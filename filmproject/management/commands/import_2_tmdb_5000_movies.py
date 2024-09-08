import csv
import json
from django.core.management.base import BaseCommand
from filmproject.models import Company, Country, Film, Genre, Keyword, Language, LT_Films_Companies, LT_Films_Countries, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages


class Command(BaseCommand):
    help = 'Import data from tmdb_5000_movies.csv into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    film_tmdb_id = int(row['id'])
                    film_title = row['title']
                    runtime_value = row.get('runtime', 0)
                    try:
                        runtime = int(float(runtime_value))
                    except ValueError:
                        runtime = 0
                    film_defaults = {
                        'budget': int(row.get('budget', 0)),
                        'homepage': row.get('homepage', ''),
                        'original_title': row.get('original_title', film_title),
                        'overview': row.get('overview', ''),
                        'popularity': float(row.get('popularity', 0.0)),
                        'release_date': row.get('release_date', None) or None,
                        'revenue': int(row.get('revenue', 0)),
                        'runtime': runtime,
                        'status': row.get('status', ''),
                        'tagline': row.get('tagline', ''),
                        'title': film_title,
                        'vote_average': float(row.get('vote_average', 0.0)),
                        'vote_count': int(row.get('vote_count', 0)),

                        # The following attributes are not in the CSV
                        'backdrop_path': row.get('backdrop_path', ''),
                        'belongs_to_collection': row.get('belongs_to_collection', '').strip().lower() == 'true',
                        'imdb_id': row.get('imdb_id', ''),
                        'poster_path': row.get('poster_path', ''),
                    }

                    film, created = Film.objects.get_or_create(
                        tmdb_id = film_tmdb_id,
                        defaults = film_defaults
                        )

                    # Extract and process genres
                    genres_json = row['genres']
                    genres_list = json.loads(genres_json)
                    for genre_data in genres_list:
                        genre_tmdb_id = genre_data['id']
                        genre_name = genre_data['name']
                        # Create or get the genre
                        genre, created = Genre.objects.get_or_create(
                            tmdb_id = genre_tmdb_id,
                            defaults={'genre': genre_name}
                            )
                        # Link the film and genre in LT_Films_Genres
                        LT_Films_Genres.objects.get_or_create(film_id=film, genre_id=genre)

                    # Extract and process keywords
                    keywords_json = row['keywords']
                    keywords_list = json.loads(keywords_json)
                    for keyword_data in keywords_list:
                        keyword_tmdb_id = keyword_data['id']
                        keyword_name = keyword_data['name']
                        # Create or get the keyword
                        keyword, created = Keyword.objects.get_or_create(
                            tmdb_id=keyword_tmdb_id,
                            defaults={'keyword': keyword_name}
                            )
                        # Link the film and keyword in LT_Films_keywords
                        LT_Films_Keywords.objects.get_or_create(
                            film_id = film,
                            keyword_id = keyword
                            )

                    # Extract and process companies
                    companies_json = row['production_companies']
                    companies_list = json.loads(companies_json)
                    for company_data in companies_list:
                        company_name = company_data.get('name')
                        company_tmdb_id = company_data.get('id')
                        # Create or get the company
                        company, created = Company.objects.get_or_create(
                            tmdb_id=company_tmdb_id, 
                            defaults={'company': company_name}
                        )
                        LT_Films_Companies.objects.get_or_create(
                            film = film,
                            company = company
                            )

                    # Extract and process countries
                    countries_json = row['production_countries']
                    countries_list = json.loads(countries_json)
                    for country_data in countries_list:
                        country_tmdb_id = country_data.get('iso_3166_1')
                        country_name = country_data.get('name')
                        country, created = Country.objects.get_or_create(
                            code=country_tmdb_id, 
                            defaults={'country': country_name}
                        )
                        LT_Films_Countries.objects.get_or_create(
                            film = film,
                            country = country
                            )

                    # Extract and process languages
                    languages_json = row['spoken_languages']
                    languages_list = json.loads(languages_json)
                    for language_data in languages_list:
                        language_tmdb_id = language_data.get('iso_639_1')
                        language_name = language_data.get('name')
                        language, created = Language.objects.get_or_create(
                            code=language_tmdb_id, 
                            defaults={'language': language_name}
                        )
                        LT_Films_Languages.objects.get_or_create(
                            film = film,
                            language = language
                            )

                    self.stdout.write(self.style.SUCCESS(f'Processed film: {film_title}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error processing film {row.get("title", "Unknown")}: {e}'))
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))