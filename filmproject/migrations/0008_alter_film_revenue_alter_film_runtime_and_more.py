# Generated by Django 5.1.2 on 2024-10-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0007_alter_viewer_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='revenue',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='runtime',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='vote_average',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]