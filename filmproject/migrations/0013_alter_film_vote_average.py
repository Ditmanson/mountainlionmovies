# Generated by Django 5.1.2 on 2024-10-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0012_alter_film_vote_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='vote_average',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
    ]
