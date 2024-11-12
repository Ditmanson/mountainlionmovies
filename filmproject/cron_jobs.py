from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import timedelta
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.db.models import Count, Q, Sum
from django.utils import timezone
from filmproject.models import Film, Viewer, LT_Viewer_Cosine_Similarity, LT_Viewer_Ratings, LT_Viewer_Seen


# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')
scheduler_running = False

def start_scheduler():
    global scheduler_running
    if not scheduler_running:
        try:
            scheduler.add_job(update_film_ratings, trigger=CronTrigger(day="*"), id="update_film_ratings", replace_existing=True)
            scheduler.add_job(recalculate_user_similarity, trigger=CronTrigger(day="*"), id="recalculate_user_similarity", replace_existing=True)
            scheduler.add_job(database_cleanup, trigger=CronTrigger(day_of_week="sun"), id="database_cleanup", replace_existing=True)
            register_events(scheduler)
            scheduler.start()
            scheduler_running = True
            print("Scheduler started successfully.")
        except Exception as e:
            print(f"Scheduler failed to start: {e}")
    else:
        print("Scheduler is already running.")

# delete viewer_ratings for any film no longer appearing in the user's seen list
def delete_invalid_viewer_ratings():
    all_viewers = Viewer.objects.all()
    for viewer in all_viewers:
        # Get the list of seen film IDs where seen_film=True
        seen_films = list(
            LT_Viewer_Seen.objects.filter(viewer=viewer, seen_film=True).values_list('film_id', flat=True)
        )
        print(f"Viewer '{viewer.name}' seen films (with seen_film=True): {seen_films}")

        if not seen_films:
            print(f"No films marked as seen for viewer '{viewer.name}'. Skipping.")
            continue

        # Retrieve all ratings for this viewer
        all_ratings = LT_Viewer_Ratings.objects.filter(viewer=viewer)
        invalid_ratings_manual = []

        # Manually check each rating
        for rating in all_ratings:
            film_a_id = rating.film_a_id
            film_b_id = rating.film_b_id

            # Check if either film_a or film_b is not in the seen films list
            if film_a_id not in seen_films or film_b_id not in seen_films:
                invalid_ratings_manual.append(rating.id)
                print(f"Invalid rating detected: ID={rating.id}, film_a={film_a_id}, film_b={film_b_id}")

        print(f"Invalid ratings for viewer '{viewer.name}' (manual check): {invalid_ratings_manual}")

        # Delete the manually identified invalid ratings
        if invalid_ratings_manual:
            deleted_count = LT_Viewer_Ratings.objects.filter(id__in=invalid_ratings_manual).delete()[0]
            print(f"Deleted {deleted_count} invalid viewer ratings for viewer '{viewer.name}'.")
        else:
            print(f"No invalid ratings found for viewer '{viewer.name}'.")

def calculate_good_viewer_ratings():
    all_viewers = Viewer.objects.all()
    for viewer in all_viewers:
        seen_films = LT_Viewer_Seen.objects.filter(viewer=viewer).values_list('film', flat=True) # Get all films in the viewer's "seen" list
        for film in seen_films:
            film_a_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_a=film).aggregate(total_a_points=Sum('a_points'), count_a=Count('id')) # Aggregate points for film_a
            total_a_points = film_a_data['total_a_points'] or 0
            count_a = film_a_data['count_a'] or 0
            film_b_data = LT_Viewer_Ratings.objects.filter(viewer=viewer, film_b=film).aggregate(total_b_points=Sum('b_points'), count_b=Count('id')) # Aggregate points for film_b
            total_b_points = film_b_data['total_b_points'] or 0
            count_b = film_b_data['count_b'] or 0
            total_points = total_a_points + total_b_points # Calculate total points and total comparisons
            total_comparisons = count_a + count_b
            viewer_rating = total_points / total_comparisons if total_comparisons > 0 else 0
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(viewer_rating=viewer_rating) # Update the LT_Viewer_Seen entry with the new viewer rating
            print(f"Updated viewer rating for film ID {film} for viewer {viewer.name}: {viewer_rating}")
    print("Viewer ratings recalculated and updated successfully.")

def recalculate_mlm_ratings():
    all_films = Film.objects.all() # Recalculates the mlm_rating for all films based on the sum of viewer ratings from LT_Viewer_Seen
    for film in all_films:
        total_viewer_ratings = (LT_Viewer_Seen.objects.filter(film=film, viewer_rating__isnull=False, seen_film=True).aggregate(total=Sum("viewer_rating"))["total"] or 0) # Calculate the total sum of viewer ratings for this film
        film.mlm_rating = total_viewer_ratings # Update the mlm_rating field of the film
        film.save()
        print(f"Updated mlm_rating for film '{film.title}': {film.mlm_rating}")
    print("MLM ratings recalculated for all films.")

def update_film_ratings():
    print("Starting film ratings update...")
    delete_invalid_viewer_ratings() # Step 1: Check each viewer's "seen" list and remove ratings if a film is no longer in it
    calculate_good_viewer_ratings() # Step 2: Calculate and update ratings for films still in viewers' seen lists
    recalculate_mlm_ratings() # Step 3: Recalculate MLM ratings
    print("Film ratings update completed.")

def database_cleanup():
    print("Database cleanup placeholder.")

def recalculate_user_similarity():
    print("User similarity matrix placeholder .")

try:
    scheduler.add_job(update_film_ratings, trigger=CronTrigger(day="*"), id="update_film_ratings", replace_existing=True) # Daily Job
    scheduler.add_job(recalculate_user_similarity, trigger=CronTrigger(day="*"), id="recalculate_user_similarity", replace_existing=True) # Daily Jobs
    scheduler.add_job(database_cleanup, trigger=CronTrigger(day_of_week="sun"), id="database_cleanup", replace_existing=True) # Weekly (Sunday) Job
    register_events(scheduler) # Register the scheduler
    scheduler.start()
    print("Scheduler started successfully.")
except Exception as e:
    print(f"Scheduler failed to start: {e}")
