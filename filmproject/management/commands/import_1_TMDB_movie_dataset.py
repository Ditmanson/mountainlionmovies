import csv
from django.core.management.base import BaseCommand
from filmproject.models import Film


class Command(BaseCommand):
    help = 'Import films from TMDB_movie_dataset_v11.csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                release_date = row.get('release_date', '').strip()
                if not release_date:
                    release_date = None
                try:
                    film, created = Film.objects.get_or_create(
                        tmdb_id=row['id'],
                        defaults={
                            'adult': row['adult'].strip().lower() == 'true',
                            'backdrop_path': row.get('backdrop_path', ''),
                            'belongs_to_collection': row.get('belongs_to_collection', '').strip().lower() == 'true',
                            'budget': row.get('budget', 0),
                            'homepage': row.get('homepage', ''),
                            'imdb_id': row.get('imdb_id', ''),
                            'original_title': row['original_title'],
                            'overview': row.get('overview', ''),
                            'popularity': row.get('popularity', 0),
                            'poster_path': row.get('poster_path', ''),
                            'release_date': release_date,
                            'revenue': row.get('revenue', 0),
                            'runtime': row.get('runtime', 0),
                            'status': row.get('status', ''),
                            'tagline': row.get('tagline', ''),
                            'title': row['title'],
                            'vote_average': row.get('vote_average', 0.0),
                            'vote_count': row.get('vote_count', 0),
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Added {film.title}'))
                    else:
                        self.stdout.write(self.style.SUCCESS(f'Processed film: {film.title}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error processing film {row.get("title", "Unknown")}: {e}'))
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))



        
