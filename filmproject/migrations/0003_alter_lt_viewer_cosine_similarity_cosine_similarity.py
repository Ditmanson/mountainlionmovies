# Generated by Django 5.1.2 on 2024-12-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0002_alter_lt_viewer_cosine_similarity_cosine_similarity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lt_viewer_cosine_similarity',
            name='cosine_similarity',
            field=models.DecimalField(decimal_places=9, max_digits=10, null=True),
        ),
    ]
