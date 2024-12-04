# Generated by Django 5.1.2 on 2024-12-04 02:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0006_lt_viewer_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lt_viewer_seen', to='filmproject.viewer'),
        ),
    ]
