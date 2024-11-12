# Generated by Django 5.1.2 on 2024-10-25 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0014_alter_person_adult_alter_person_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_films_cast',
            name='character',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='credit_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='film',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.film'),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lt_films_cast',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='filmproject.person'),
        ),
    ]