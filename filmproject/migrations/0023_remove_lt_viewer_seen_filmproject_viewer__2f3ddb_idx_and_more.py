from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmproject', '0022_film_mlm_rating'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='lt_viewer_seen',
            name='filmproject_viewer__2f3ddb_idx',
        ),
        migrations.AlterField(
            model_name='lt_viewer_seen',
            name='viewer_rating',
            field=models.DecimalField(decimal_places=8, default=0.5, max_digits=9, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='lt_viewer_seen',
            unique_together={('viewer', 'film')},
        ),
    ]
