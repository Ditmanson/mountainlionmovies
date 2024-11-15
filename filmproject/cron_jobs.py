import numpy as np
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.db.models import Sum
from filmproject.models import (
    Film,
    Viewer,
    LT_Viewer_Cosine_Similarity,
    LT_Viewer_Ratings,
    LT_Viewer_Seen,
)

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler_running = False


def start_scheduler():
    global scheduler_running
    if not scheduler_running:
        try:
            scheduler.add_job(
                update_film_ratings,
                trigger=CronTrigger(day="*"),
                id="update_film_ratings",
                replace_existing=True,
            )
            scheduler.add_job(
                calculate_cosine_similarity,
                trigger=CronTrigger(day="*"),
                id="calculate_cosine_similarity",
                replace_existing=True,
            )
            scheduler.add_job(
                database_cleanup,
                trigger=CronTrigger(day_of_week="sun"),
                id="database_cleanup",
                replace_existing=True,
            )
            register_events(scheduler)
            scheduler.start()
            scheduler_running = True
            print("Scheduler started successfully.")
        except Exception as e:
            print(f"Scheduler failed to start: {e}")
    else:
        print("Scheduler is already running.")


def delete_invalid_viewer_ratings():
    all_viewers = Viewer.objects.all()
    for viewer in all_viewers:
        seen_films = list(
            LT_Viewer_Seen.objects.filter(
                viewer=viewer, seen_film=True
            ).values_list("film_id", flat=True)
        )
        print(f"Viewer '{viewer.name}' seen films: {seen_films}")
        if not seen_films:
            print(
                f"No films marked as seen for viewer '{
                    viewer.name}'. Skipping."
            )
            continue

        all_ratings = LT_Viewer_Ratings.objects.filter(viewer=viewer)
        invalid_ratings = [
            rating.id
            for rating in all_ratings
            if rating.film_a_id not in seen_films
            or rating.film_b_id not in seen_films
        ]
        if invalid_ratings:
            deleted_count = LT_Viewer_Ratings.objects.filter(
                id__in=invalid_ratings
            ).delete()[0]
            print(
                f"Deleted {deleted_count} invalid viewer ratings for viewer '{
                    viewer.name}'."
            )


def calculate_cosine_similarity():
    viewers = list(Viewer.objects.all())
    for i, viewer_1 in enumerate(viewers):
        for j, viewer_2 in enumerate(viewers):
            if i >= j:
                continue

            ratings_1 = dict(
                LT_Viewer_Seen.objects.filter(
                    viewer=viewer_1, seen_film=True
                ).values_list("film_id", "viewer_rating")
            )
            ratings_2 = dict(
                LT_Viewer_Seen.objects.filter(
                    viewer=viewer_2, seen_film=True
                ).values_list("film_id", "viewer_rating")
            )
            common_films = set(ratings_1.keys()) & set(ratings_2.keys())

            if common_films:
                vector_1 = np.array([ratings_1[film] for film in common_films])
                vector_2 = np.array([ratings_2[film] for film in common_films])

                norm_1 = np.linalg.norm(vector_1)
                norm_2 = np.linalg.norm(vector_2)
                similarity_score = (
                    np.dot(vector_1, vector_2) / (norm_1 * norm_2)
                    if norm_1 and norm_2
                    else 0.0
                )
            else:
                similarity_score = 0.0

            LT_Viewer_Cosine_Similarity.objects.update_or_create(
                viewer_1=viewer_1,
                viewer_2=viewer_2,
                defaults={"cosine_similarity": round(similarity_score, 4)},
            )
            print(
                f"Updated similarity for {
                    viewer_1.name} and {
                    viewer_2.name}: {similarity_score}"
            )


def calculate_mlm_ratings():
    for film in Film.objects.all():
        total_viewer_ratings = (
            LT_Viewer_Seen.objects.filter(
                film=film, viewer_rating__isnull=False, seen_film=True
            ).aggregate(total=Sum("viewer_rating"))["total"]
            or 0
        )
        film.mlm_rating = total_viewer_ratings
        film.save()
        print(f"Updated mlm_rating for film '{film.title}': {film.mlm_rating}")


def update_film_ratings():
    print("Starting film ratings update...")
    delete_invalid_viewer_ratings()
    calculate_cosine_similarity()
    calculate_mlm_ratings()
    print("Film ratings update completed.")


def database_cleanup():
    print("Database cleanup placeholder.")


try:
    scheduler.add_job(
        update_film_ratings,
        trigger=CronTrigger(day="*"),
        id="update_film_ratings",
        replace_existing=True,
    )
    scheduler.add_job(
        calculate_cosine_similarity,
        trigger=CronTrigger(day="*"),
        id="calculate_cosine_similarity",
        replace_existing=True,
    )
    scheduler.add_job(
        database_cleanup,
        trigger=CronTrigger(day_of_week="sun"),
        id="database_cleanup",
        replace_existing=True,
    )
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started successfully.")
except Exception as e:
    print(f"Scheduler failed to start: {e}")
