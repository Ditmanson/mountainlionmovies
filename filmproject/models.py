from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Collection(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    feed_entry = models.ForeignKey("FeedEntry", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Company(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    company = models.CharField(max_length=200)
    def __str__(self):
        return self.company

class Country(models.Model):
    code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.country

class FeedEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey("Film", on_delete=models.CASCADE)  # Reference Film by string
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class Film(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)
    belongs_to_collection = models.BooleanField(default=False)
    budget = models.IntegerField(null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    imdb_id = models.CharField(max_length=20, blank=True, null=True)
    original_title = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000, blank=True, null=True)
    popularity = models.DecimalField(decimal_places=6, max_digits=20)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    revenue = models.BigIntegerField(null=True)
    runtime = models.IntegerField(null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    tagline = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    tmdb_id = models.IntegerField(unique=True, null=True)
    vote_average = models.DecimalField(decimal_places=3, max_digits=6, null=True, blank=True)
    vote_count = models.IntegerField(null=True)
    mlm_rating = models.DecimalField(decimal_places=6, max_digits=20, null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("film-detail", args=[str(self.id)])

class FriendRequest(models.Model):
    sender = models.ForeignKey("Viewer", related_name="sent_requests", on_delete=models.CASCADE)
    receiver = models.ForeignKey("Viewer", related_name="received_requests", on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True)
    rejected_at = models.DateTimeField(null=True)
    def accept(self):
        self.status = "accepted"
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()
    def reject(self):
        self.status = "rejected"
        self.save()
    def __str__(self):
        return f"{self.sender.name} -> {self.receiver.name} ({self.status})"
    
class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    genre = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.genre

class Keyword(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    keyword = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.keyword

class Language(models.Model):
    code = models.CharField(null=True, unique=True, max_length=4)
    language = models.CharField(null=True, max_length=200)
    def __str__(self):
        return self.language

class Like(models.Model):
    feed_entry = models.ForeignKey("FeedEntry", related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LT_Films_Cast(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING, null=True)
    person = models.ForeignKey("Person", on_delete=models.DO_NOTHING, null=True)
    cast_id = models.IntegerField()
    character = models.CharField(null=True, max_length=200)
    credit_id = models.CharField(max_length=200, null=True)
    order = models.IntegerField(null=True)

class LT_Films_Companies(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    company = models.ForeignKey("Company", on_delete=models.DO_NOTHING)

class LT_Films_Countries(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    country = models.ForeignKey("Country", on_delete=models.DO_NOTHING)

class LT_Films_Crew(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING, null=True)
    person = models.ForeignKey("Person", on_delete=models.DO_NOTHING, null=True)
    credit_id = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)

class LT_Films_Genres(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    genre = models.ForeignKey("Genre", on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ("film", "genre")

class LT_Films_Keywords(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    keyword = models.ForeignKey("Keyword", on_delete=models.DO_NOTHING)
    def get_absolute_url(self):
        return reverse("LT_Films_Keywords-detail", args=[str(self.id)])
    class Meta:
        unique_together = ("film", "keyword")

class LT_Films_Languages(models.Model):
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    language = models.ForeignKey("Language", on_delete=models.DO_NOTHING)

class LT_Viewer_Cosine_Similarity(models.Model):
    viewer_1 = models.ForeignKey("Viewer", on_delete=models.PROTECT, related_name="viewer_1")
    viewer_2 = models.ForeignKey("Viewer", on_delete=models.PROTECT, related_name="viewer_2")
    cosine_similarity = models.DecimalField(decimal_places=8, max_digits=9, null=True)
    class Meta:
        unique_together = ("viewer_1", "viewer_2")

class LT_Viewer_Ratings(models.Model):
    viewer = models.ForeignKey("Viewer", on_delete=models.DO_NOTHING, null=True)
    film_a = models.ForeignKey("Film", on_delete=models.DO_NOTHING, related_name="film_a", null=True)
    film_b = models.ForeignKey("Film", on_delete=models.DO_NOTHING, related_name="film_b", null=True)
    date = models.DateField(default=date.today, null=True)
    a_points = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    b_points = models.DecimalField(decimal_places=1, max_digits=3, null=True)
    class Meta:
        unique_together = ("viewer", "film_a", "film_b")

class LT_Viewer_Recommendations(models.Model):
    viewer = models.ForeignKey("Viewer", on_delete=models.DO_NOTHING, null=True)
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING, related_name="recommended_film", null=True)
    recommendation_score = models.DecimalField(decimal_places=8, max_digits=9, null=True)
    class Meta:
        unique_together = ("viewer", "film")

class LT_Viewer_Seen(models.Model):
    viewer = models.ForeignKey("Viewer", on_delete=models.DO_NOTHING, null=True, related_name="lt_viewer_seen")
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING, null=True)
    seen_film = models.BooleanField(default=False, null=True)
    viewer_rating = models.DecimalField(decimal_places=8, max_digits=9, default=0.5, null=True)
    class Meta:
        unique_together = ("viewer", "film")

class LT_Viewer_Watchlist(models.Model):
    viewer = models.ForeignKey("Viewer", on_delete=models.DO_NOTHING, related_name="lt_viewer_watchlist")
    film = models.ForeignKey("Film", on_delete=models.DO_NOTHING)
    watchlist = models.BooleanField(default=False)
    class Meta:
        unique_together = ("viewer", "film")

# class Notification(models.Model):
#     TYPE_CHOICES = [("like", "Like"), ("comment", "Comment")]
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="notifications")
#     feed_entry = models.ForeignKey("FeedEntry", on_delete=models.CASCADE)
#     notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
#     is_read = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.user.username} - {self.notification_type} on {self.feed_entry}"
    
class Person(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    tmdb_id = models.IntegerField(unique=True)
    known_for_department = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    popularity = models.DecimalField(decimal_places=3, null=True, blank=True, max_digits=10)
    profile_path = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("person-detail", args=[str(self.id)])

class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='viewer')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True, default="profile_pictures/default_pfp.jpg")
    friends = models.ManyToManyField("self", blank=True)
    def add_friend(self, viewer):
        if not self.is_friends_with(viewer):
            self.friends.add(viewer)
            self.save()
    def has_seen_film(self, film):
        return self.lt_viewer_seen.filter(film=film, seen_film=True).exists()
    def is_friends_with(self, viewer):
        return self.friends.filter(id=viewer.id).exists()
    def is_in_watchlist(self, film):
        return self.lt_viewer_watchlist.filter(film=film, watchlist=True).exists()
    def remove_friend(self, viewer):
        if self.is_friends_with(viewer):
            self.friends.remove(viewer)
            self.save()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("profile_viewer", args=[str(self.id)])
