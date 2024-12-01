from datetime import date
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class LT_Films_Cast(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING, null=True)
    person = models.ForeignKey("filmproject.Person", on_delete=models.DO_NOTHING, null=True)
    cast_id = models.IntegerField()
    character = models.CharField(null=True, max_length=200)
    credit_id = models.CharField(max_length=200, null=True)
    order = models.IntegerField(null=True)

class LT_Films_Companies(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    company = models.ForeignKey("filmproject.Company", on_delete=models.DO_NOTHING)

class LT_Films_Countries(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    country = models.ForeignKey("filmproject.Country", on_delete=models.DO_NOTHING)

class LT_Films_Crew(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING, null=True)
    person = models.ForeignKey("filmproject.Person", on_delete=models.DO_NOTHING, null=True)
    credit_id = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)

class LT_Films_Genres(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    genre = models.ForeignKey("filmproject.Genre", on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ("film", "genre")

class LT_Films_Keywords(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    keyword = models.ForeignKey("filmproject.Keyword", on_delete=models.DO_NOTHING)
    def get_absolute_url(self):
        return reverse("LT_Films_Keywords-detail", args=[str(self.id)])
    class Meta:
        unique_together = ("film", "keyword")

class LT_Films_Languages(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    language = models.ForeignKey("filmproject.Language", on_delete=models.DO_NOTHING)

class LT_Viewer_Cosine_Similarity(models.Model):
    viewer_1 = models.ForeignKey("filmproject.Viewer", on_delete=models.PROTECT, related_name="viewer_1")
    viewer_2 = models.ForeignKey("filmproject.Viewer", on_delete=models.PROTECT, related_name="viewer_2")
    cosine_similarity = models.DecimalField(decimal_places=4, max_digits=5, null=True)
    class Meta:
        unique_together = ("viewer_1", "viewer_2")

class LT_Viewer_Ratings(models.Model):
    viewer = models.ForeignKey("filmproject.Viewer", on_delete=models.DO_NOTHING, null=True)
    film_a = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING, related_name="film_a", null=True)
    film_b = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING, related_name="film_b", null=True)
    date = models.DateField(default=date.today, null=True)
    a_points = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    b_points = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    class Meta:
        unique_together = ("viewer", "film_a", "film_b")


class LT_Viewer_Seen(models.Model):
    viewer = models.ForeignKey("filmproject.Viewer", on_delete=models.DO_NOTHING, null=True)
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING, null=True)
    seen_film = models.BooleanField(default=False, null=True)
    viewer_rating = models.DecimalField(decimal_places=8, max_digits=9, default=0.5, null=True)
    class Meta:
        unique_together = ("viewer", "film")


class LT_Viewer_Watchlist(models.Model):
    viewer = models.ForeignKey("filmproject.Viewer", on_delete=models.DO_NOTHING)
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    watchlist = models.BooleanField(default=False)
    class Meta:
        unique_together = ("viewer", "film")
