# Generated by Django 5.1.2 on 2024-10-21 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0002_alter_lt_viewer_seen_film_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lt_viewer_seen',
            name='viewer_rating',
        ),
    ]
