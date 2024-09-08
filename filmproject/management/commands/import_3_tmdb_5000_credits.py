import csv
import json
from django.core.management.base import BaseCommand
from filmproject.models import Film, LT_Films_Cast, LT_Films_Crew, Person

class Command(BaseCommand):
    help = 'Import people from tmdb_5000_credits.csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    film_tmdb_id = int(row['movie_id'])
                    film_title = row['title']
                    film_defaults = {
                        'title': film_title,
                    }

                    # Create or get the film
                    film, created = Film.objects.get_or_create(tmdb_id = film_tmdb_id, defaults = film_defaults)

                    # Extract and process cast
                    cast_json = row['cast']
                    cast_list = json.loads(cast_json)
                    for cast_data in cast_list:
                        cast_cast_id = cast_data['cast_id']
                        cast_character = cast_data['character']
                        cast_credit_id = cast_data['credit_id']
                        cast_gender = cast_data['gender']
                        cast_tmdb_id = cast_data['id']
                        cast_name = cast_data['name']
                        cast_order = cast_data['order']

                        # Create or get the cast member
                        cast, created = Person.objects.get_or_create(
                              adult = False,
                              gender = cast_gender,
                              tmdb_id = cast_tmdb_id,
                              known_for_department = '',
                              name = cast_name,
                              popularity = 0,
                              profile_path = '')
                        
                        # Link the film and keyword in LT_Films_Cast
                        LT_Films_Cast.objects.get_or_create(
                              film_id = film.id,
                              person_id = cast.id,
                              cast_id = cast_cast_id,
                              character = cast_character,
                              credit_id = cast_credit_id,
                              order = cast_order
                              )

                    # Extract and process crew
                    crew_json = row['crew']
                    crew_list = json.loads(crew_json)
                    for crew_data in crew_list:
                        crew_credit_id = crew_data['credit_id']
                        crew_department = crew_data['department']
                        crew_gender = crew_data['gender']
                        crew_tmdb_id = crew_data['id']
                        crew_job = crew_data['job']
                        crew_name = crew_data['name']

                        # Create or get the crew member
                        crew, created = Person.objects.get_or_create(
                              adult = False,
                              gender = crew_gender,
                              tmdb_id = crew_tmdb_id,
                              known_for_department = '',
                              name = crew_name,
                              popularity = 0,
                              profile_path = '')
                        
                        # Link the film and keyword in LT_Films_crew
                        LT_Films_Crew.objects.get_or_create(
                              film_id = film.id,
                              person_id = crew.id,
                              credit_id = crew_credit_id,
                              department = crew_department,
                              job = crew_job
                              )

                    self.stdout.write(self.style.SUCCESS(f'Processed film: {film_title}'))
                except Exception as e:
                    # Log the error and continue processing the next row
                    self.stderr.write(self.style.ERROR(f'Error processing film {row.get("title", "Unknown")}: {e}'))
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))