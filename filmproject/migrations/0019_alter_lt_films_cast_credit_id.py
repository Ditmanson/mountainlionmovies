# Generated by Django 5.0.7 on 2024-09-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0018_alter_language_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_films_cast',
            name='credit_id',
            field=models.CharField(max_length=200),
        ),
    ]
