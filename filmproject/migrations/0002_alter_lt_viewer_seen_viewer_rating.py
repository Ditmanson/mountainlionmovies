# Generated by Django 5.1.2 on 2024-10-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='viewer_rating',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=9, null=True),
        ),
    ]