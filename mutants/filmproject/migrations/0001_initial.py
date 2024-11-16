
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


# Generated by Django 5.1.2 on 2024-11-12 23:55
# noqa: E501

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tmdb_id", models.IntegerField()),
                ("name", models.CharField(max_length=200)),
                (
                    "poster_path",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "backdrop_path",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tmdb_id", models.IntegerField(null=True, unique=True)),
                ("company", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("adult", models.BooleanField(blank=True, null=True)),
                (
                    "backdrop_path",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("belongs_to_collection", models.BooleanField(default=False)),
                ("budget", models.IntegerField(null=True)),
                (
                    "homepage",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "imdb_id",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("original_title", models.CharField(max_length=200)),
                (
                    "overview",
                    models.CharField(blank=True, max_length=2000, null=True),
                ),
                (
                    "popularity",
                    models.DecimalField(decimal_places=6, max_digits=20),
                ),
                (
                    "poster_path",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("release_date", models.DateField(blank=True, null=True)),
                ("revenue", models.BigIntegerField(null=True)),
                ("runtime", models.IntegerField(null=True)),
                (
                    "status",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "tagline",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("title", models.CharField(max_length=200)),
                ("tmdb_id", models.IntegerField(null=True, unique=True)),
                (
                    "vote_average",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=6, null=True
                    ),
                ),
                ("vote_count", models.IntegerField(null=True)),
                (
                    "mlm_rating",
                    models.DecimalField(
                        decimal_places=6, max_digits=20, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tmdb_id", models.IntegerField(null=True, unique=True)),
                ("genre", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Keyword",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tmdb_id", models.IntegerField(null=True, unique=True)),
                ("keyword", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(max_length=4, null=True, unique=True),
                ),
                ("language", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("adult", models.BooleanField(blank=True, null=True)),
                ("gender", models.IntegerField(blank=True, null=True)),
                ("tmdb_id", models.IntegerField(unique=True)),
                (
                    "known_for_department",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "popularity",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=10, null=True
                    ),
                ),
                (
                    "profile_path",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="filmproject.film",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "feed_entry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="filmproject.feedentry",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "feed_entry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="filmproject.feedentry",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Companies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.company",
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Countries",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.country",
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Languages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.language",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notification_type",
                    models.CharField(
                        choices=[("like", "Like"), ("comment", "Comment")],
                        max_length=10,
                    ),
                ),
                ("is_read", models.BooleanField(default=False)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "feed_entry",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="filmproject.feedentry",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Crew",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("credit_id", models.CharField(max_length=200, null=True)),
                ("department", models.CharField(max_length=200, null=True)),
                ("job", models.CharField(max_length=200, null=True)),
                (
                    "film",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Cast",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cast_id", models.IntegerField()),
                ("character", models.CharField(max_length=200, null=True)),
                ("credit_id", models.CharField(max_length=200, null=True)),
                ("order", models.IntegerField(null=True)),
                (
                    "film",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Viewer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        default="profile_pictures/default_pfp.jpg",
                        null=True,
                        upload_to="profile_pictures/",
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, to="filmproject.viewer"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FriendRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("accepted", "Accepted"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("accepted_at", models.DateTimeField(null=True)),
                ("rejected_at", models.DateTimeField(null=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_requests",
                        to="filmproject.viewer",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_requests",
                        to="filmproject.viewer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LT_Films_Genres",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.genre",
                    ),
                ),
            ],
            options={
                "unique_together": {("film", "genre")},
            },
        ),
        migrations.CreateModel(
            name="LT_Films_Keywords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "keyword",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.keyword",
                    ),
                ),
            ],
            options={
                "unique_together": {("film", "keyword")},
            },
        ),
        migrations.CreateModel(
            name="LT_Viewer_Watchlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("watchlist", models.BooleanField(default=False)),
                (
                    "film",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.viewer",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["viewer", "film"],
                        name="filmproject_viewer__159eba_idx",
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="LT_Viewer_Seen",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seen_film", models.BooleanField(default=False, null=True)),
                (
                    "viewer_rating",
                    models.DecimalField(
                        decimal_places=8, default=0.5, max_digits=9, null=True
                    ),
                ),
                (
                    "film",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.film",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.viewer",
                    ),
                ),
            ],
            options={
                "unique_together": {("viewer", "film")},
            },
        ),
        migrations.CreateModel(
            name="LT_Viewer_Ratings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(default=datetime.date.today, null=True),
                ),
                (
                    "a_points",
                    models.DecimalField(
                        decimal_places=1, default=0, max_digits=3, null=True
                    ),
                ),
                (
                    "b_points",
                    models.DecimalField(
                        decimal_places=1, default=0, max_digits=3, null=True
                    ),
                ),
                (
                    "film_a",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="film_a",
                        to="filmproject.film",
                    ),
                ),
                (
                    "film_b",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="film_b",
                        to="filmproject.film",
                    ),
                ),
                (
                    "viewer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filmproject.viewer",
                    ),
                ),
            ],
            options={
                "unique_together": {("viewer", "film_a", "film_b")},
            },
        ),
        migrations.CreateModel(
            name="LT_Viewer_Cosine_Similarity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cosine_similarity",
                    models.DecimalField(
                        decimal_places=4, max_digits=6, null=True
                    ),
                ),
                (
                    "viewer_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="viewer_1",
                        to="filmproject.viewer",
                    ),
                ),
                (
                    "viewer_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="viewer_2",
                        to="filmproject.viewer",
                    ),
                ),
            ],
            options={
                "unique_together": {("viewer_1", "viewer_2")},
            },
        ),
    ]
