# Generated by Django 5.1.2 on 2024-12-04 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0007_alter_lt_viewer_seen_viewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_viewer_watchlist',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='lt_viewer_watchlist', to='filmproject.viewer'),
        ),
    ]
