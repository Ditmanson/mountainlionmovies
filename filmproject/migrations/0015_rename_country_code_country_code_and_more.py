# Generated by Django 5.0.7 on 2024-08-25 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0014_alter_country_country_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='country_name',
            new_name='country',
        ),
    ]
