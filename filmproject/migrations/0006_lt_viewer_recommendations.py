# Generated by Django 5.1.2 on 2024-12-01 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0005_alter_viewer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LT_Viewer_Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_score', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommended_film', to='filmproject.film')),
                ('viewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.viewer')),
            ],
            options={
                'unique_together': {('viewer', 'film')},
            },
        ),
    ]
