# Generated by Django 5.1.2 on 2024-10-21 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='seen_film',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='viewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.viewer'),
        ),
    ]
