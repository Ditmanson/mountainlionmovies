# Generated by Django 5.0.7 on 2024-08-25 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0004_alter_film_tmdb_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lt_films_genres',
            unique_together={('film_id', 'genre_id')},
        ),
    ]
