# Generated by Django 5.0.7 on 2024-08-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0003_alter_genre_tmdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='tmdb_id',
            field=models.IntegerField(unique=True),
        ),
    ]
