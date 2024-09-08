# Generated by Django 5.0.7 on 2024-08-25 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='tmdb_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lt_viewer_ratings',
            name='user_rating',
            field=models.DecimalField(decimal_places=8, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.person'),
        ),
        migrations.AlterField(
            model_name='lt_films_companies',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.company'),
        ),
        migrations.AlterField(
            model_name='lt_films_companies',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_countries',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.country'),
        ),
        migrations.AlterField(
            model_name='lt_films_countries',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_crew',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_crew',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.person'),
        ),
        migrations.AlterField(
            model_name='lt_films_genres',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_genres',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.genre'),
        ),
        migrations.AlterField(
            model_name='lt_films_keywords',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_keywords',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.keyword'),
        ),
        migrations.AlterField(
            model_name='lt_films_languages',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_languages',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.language'),
        ),
        migrations.AlterField(
            model_name='lt_viewer_ratings',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_viewer_ratings',
            name='viewer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.viewer'),
        ),
        migrations.CreateModel(
            name='LT_Seen_Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen_film', models.BooleanField(default=False)),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film')),
                ('viewer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.viewer')),
            ],
        ),
    ]
