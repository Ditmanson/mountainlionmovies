# Generated by Django 5.1.2 on 2024-10-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0016_alter_lt_films_crew_credit_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lt_viewer_ratings',
            name='b_points',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True),
        ),
    ]