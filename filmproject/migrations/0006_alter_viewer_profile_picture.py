# Generated by Django 5.1.2 on 2024-10-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0005_alter_lt_viewer_ratings_a_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='profile_picture',
            field=models.ImageField(blank=True, default='https://plus.unsplash.com/premium_photo-1728391710545-3d7d0bcd0b21?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwyfHx8ZW58MHx8fHx8', null=True, upload_to='profile_pictures/'),
        ),
    ]
