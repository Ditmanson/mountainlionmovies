from django.core.management.base import BaseCommand
from filmproject.models import Film


class Command(BaseCommand):
    help = "Update MLM ratings for all films"

    def handle(self, *args, **kwargs):
        films = Film.objects.all()
        for film in films:
            film.update_mlm_rating()
            self.stdout.write(f"Updated MLM rating for: {film.title}")
