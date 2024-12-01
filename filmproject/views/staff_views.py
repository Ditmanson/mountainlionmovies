import numpy as np
from ..models import Film, LT_Viewer_Cosine_Similarity, LT_Viewer_Ratings, LT_Viewer_Recommendations, LT_Viewer_Seen, Viewer
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render

def calculate_mlm_ratings():
    total_viewers = Viewer.objects.count()
    if total_viewers == 0:
        return
    for film in Film.objects.all():
        total_viewer_ratings = (LT_Viewer_Seen.objects.filter(film=film, viewer_rating__isnull=False, seen_film=True).aggregate(total=Sum("viewer_rating"))["total"] or 0)
        film.mlm_rating = total_viewer_ratings / total_viewers # Normalize the mlm_rating by dividing by the total number of viewers
        film.save()
        print(f"Updated mlm_rating for film '{film.title}': {film.mlm_rating}")

def calculate_cosine_similarity():
    viewers = list(Viewer.objects.all())
    for i, viewer_1 in enumerate(viewers):
        for j, viewer_2 in enumerate(viewers):
            if i >= j:
                continue
            ratings_1 = dict(LT_Viewer_Seen.objects.filter(viewer=viewer_1, seen_film=True).values_list("film_id", "viewer_rating"))
            ratings_2 = dict(LT_Viewer_Seen.objects.filter(viewer=viewer_2, seen_film=True).values_list("film_id", "viewer_rating"))
            common_films = set(ratings_1.keys()) & set(ratings_2.keys())
            if common_films:
                vector_1 = np.array([ratings_1[film] for film in common_films])
                vector_2 = np.array([ratings_2[film] for film in common_films])
                norm_1 = np.linalg.norm(vector_1)
                norm_2 = np.linalg.norm(vector_2)
                similarity_score = (np.dot(vector_1, vector_2) / (norm_1 * norm_2)
                    if norm_1 and norm_2
                    else 0.0
                )
            else:
                similarity_score = 0.0
            LT_Viewer_Cosine_Similarity.objects.update_or_create(viewer_1=viewer_1, viewer_2=viewer_2, defaults={"cosine_similarity": round(similarity_score, 4)})
            print(f"Updated similarity for {viewer_1.name} and {viewer_2.name}: {similarity_score}")

def database_cleanup():
    print("Database cleanup placeholder.")

def delete_invalid_viewer_ratings():
    all_viewers = Viewer.objects.all()
    for viewer in all_viewers:
        seen_films = list(LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film_id", flat=True))
        print(f"Viewer '{viewer.name}' seen films: {seen_films}")
        if not seen_films:
            print(f"No films marked as seen for viewer '{viewer.name}'. Skipping.")
            continue
        all_ratings = LT_Viewer_Ratings.objects.filter(viewer=viewer)
        invalid_ratings = [rating.id for rating in all_ratings if rating.film_a_id not in seen_films or rating.film_b_id not in seen_films]
        if invalid_ratings:
            deleted_count = LT_Viewer_Ratings.objects.filter(id__in=invalid_ratings).delete()[0]
            print(f"Deleted {deleted_count} invalid viewer ratings for viewer '{viewer.name}'.")

@staff_member_required
def manual_update_film_ratings(request):
    try:
        update_film_ratings()
        return JsonResponse({"success": True, "message": "Film ratings updated successfully."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})

@staff_member_required
def manual_update_film_ratings(request):
    if request.method == "POST":
        try:
            update_film_ratings()
            messages.success(request, "Film ratings updated successfully.")
        except Exception as e:
            messages.error(request, f"Error updating film ratings: {e}")
    return redirect('staff_dashboard')

@staff_member_required
def manual_calculate_cosine_similarity(request):
    if request.method == "POST":
        try:
            calculate_cosine_similarity()
            messages.success(request, "Cosine similarity recalculated successfully.")
        except Exception as e:
            messages.error(request, f"Error recalculating cosine similarity: {e}")
    return redirect('staff_dashboard')

@staff_member_required
def manual_database_cleanup(request):
    if request.method == "POST":
        try:
            database_cleanup()
            messages.success(request, "Database cleanup completed successfully.")
        except Exception as e:
            messages.error(request, f"Error during database cleanup: {e}")
    return redirect('staff_dashboard')

@staff_member_required
def manual_recalculate_recommendations(request):
    from ..models import LT_Viewer_Cosine_Similarity, LT_Viewer_Recommendations, LT_Viewer_Seen, Film
    if request.method == "POST":
        try:
            # Clear existing recommendations
            LT_Viewer_Recommendations.objects.all().delete()
            # Logic for generating recommendations
            viewers = Viewer.objects.all()
            for viewer in viewers:
                seen_movies = LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list("film", flat=True)
                similar_viewers = LT_Viewer_Cosine_Similarity.objects.filter(
                    Q(viewer_1=viewer) | Q(viewer_2=viewer)
                ).exclude(cosine_similarity__isnull=True).order_by('-cosine_similarity')
                film_scores = {}
                for sim in similar_viewers:
                    # Identify the other viewer in the similarity record
                    other_viewer = sim.viewer_2 if sim.viewer_1 == viewer else sim.viewer_1
                    # Get movies seen by the similar user but not yet seen by the current user
                    other_seen_movies = LT_Viewer_Seen.objects.filter(
                        viewer=other_viewer, seen_film=True
                    ).exclude(film__in=seen_movies)
                    for movie_entry in other_seen_movies:
                        film = movie_entry.film
                        viewer_rating = movie_entry.viewer_rating or 0.5  # Default to neutral rating if not available
                        # Add weighted score: (Cosine Similarity) × (Viewer Rating)
                        film_scores[film] = film_scores.get(film, 0) + float(sim.cosine_similarity) * float(viewer_rating)
                # Save top recommendations for the viewer
                for film, score in sorted(film_scores.items(), key=lambda x: -x[1])[:10]:
                    LT_Viewer_Recommendations.objects.create(
                        viewer=viewer, 
                        film=film, 
                        recommendation_score=round(score, 1)
                    )
            messages.success(request, "Movie recommendations have been recalculated successfully.")
        except Exception as e:
            messages.error(request, f"Error recalculating recommendations: {e}")
        return redirect('staff_dashboard')
    
@staff_member_required
def staff_dashboard(request):
    return render(request, 'filmproject/staff_dashboard.html')

def update_film_ratings():
    print("Starting film ratings update...")
    delete_invalid_viewer_ratings()
    calculate_cosine_similarity()
    calculate_mlm_ratings()
    print("Film ratings update completed.")



# # Initialize the scheduler
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
# scheduler_running = False

# def start_scheduler():
#     global scheduler_running
#     if not scheduler_running:
#         try:
#             scheduler.add_job(update_film_ratings, trigger=CronTrigger(day="*"), id="update_film_ratings", replace_existing=True)
#             scheduler.add_job(calculate_cosine_similarity, trigger=CronTrigger(day="*"), id="calculate_cosine_similarity", replace_existing=True)
#             scheduler.add_job(database_cleanup, trigger=CronTrigger(day_of_week="sun"), id="database_cleanup", replace_existing=True)
#             register_events(scheduler)
#             scheduler.start()
#             scheduler_running = True
#             print("Scheduler started successfully.")
#         except Exception as e:
#             print(f"Scheduler failed to start: {e}")
#     else:
#         print("Scheduler is already running.")

# try:
#     scheduler.add_job(update_film_ratings, trigger=CronTrigger(day="*"), id="update_film_ratings", replace_existing=True,)
#     scheduler.add_job(calculate_cosine_similarity, trigger=CronTrigger(day="*"), id="calculate_cosine_similarity", replace_existing=True)
#     scheduler.add_job(database_cleanup, trigger=CronTrigger(day_of_week="sun"), id="database_cleanup", replace_existing=True)
#     register_events(scheduler)
#     scheduler.start()
#     print("Scheduler started successfully.")
# except Exception as e:
#     print(f"Scheduler failed to start: {e}")