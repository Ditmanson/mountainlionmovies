# Generated by Django 5.0.7 on 2024-08-24 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('poster_path', models.CharField(max_length=200)),
                ('backdrop_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=2)),
                ('country_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=200)),
                ('belongs_to_collection', models.BooleanField()),
                ('budget', models.IntegerField()),
                ('homepage', models.CharField(max_length=200)),
                ('imdb_id', models.CharField(max_length=20)),
                ('original_title', models.CharField(max_length=200)),
                ('overview', models.CharField(max_length=2000)),
                ('popularity', models.DecimalField(decimal_places=6, max_digits=20)),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('revenue', models.BigIntegerField()),
                ('runtime', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('tmdb_id', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=1, max_digits=5)),
                ('vote_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField()),
                ('keyword', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=2)),
                ('language_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('person_id', models.IntegerField()),
                ('cast_id', models.IntegerField()),
                ('character', models.CharField(max_length=200)),
                ('credit_id', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('company_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('country_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('person_id', models.IntegerField()),
                ('credit_id', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('genre_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('keyword_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Films_Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.IntegerField()),
                ('language_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LT_Viewer_Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_id', models.IntegerField()),
                ('film_id', models.IntegerField()),
                ('number_times_selected', models.IntegerField()),
                ('number_times_reviewed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('gender', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('known_for_department', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('popularity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('profile_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Viewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
            ],
        ),
    ]
