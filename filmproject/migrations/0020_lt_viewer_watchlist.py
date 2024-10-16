# Generated by Django 5.1.2 on 2024-10-13 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0019_alter_lt_films_cast_credit_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LT_Viewer_Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchlist', models.BooleanField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.viewer')),
            ],
        ),
    ]
