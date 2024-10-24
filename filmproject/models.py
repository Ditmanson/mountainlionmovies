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
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

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

class Person(models.Model):
    adult = models.BooleanField()
    gender = models.IntegerField()
    tmdb_id = models.IntegerField(unique=True)
    known_for_department = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    popularity = models.DecimalField(decimal_places=3, max_digits=10)
    profile_path = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])

class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', 
                                        blank=True, 
                                        null=True, 
                                        default='profile_pictures/default_pfp.jpg')  # Set default image
    friends = models.ManyToManyField('self', blank=True)
    def has_seen_film(self, film):
        return LT_Viewer_Seen.objects.filter(viewer=self, film=film, seen_film=True).exists()
    def is_in_watchlist(self, film):
        return LT_Viewer_Watchlist.objects.filter(viewer=self, film=film, watchlist=True).exists()    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('profile_viewer', args=[str(self.id)])
    
    def add_friend(self, viewer):
        """Add a viewer to the friends list."""
        if not self.is_friends_with(viewer):
            self.friends.add(viewer)
            self.save()

    def remove_friend(self, viewer):
        """Remove a viewer from the friends list."""
        if self.is_friends_with(viewer):
            self.friends.remove(viewer)
            self.save()

    def is_friends_with(self, viewer):
        """Check if the viewer is friends with another viewer."""
        return self.friends.filter(id=viewer.id).exists()

class LT_Films_Cast(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    cast_id = models.IntegerField()
    character = models.CharField(max_length=200)
    credit_id = models.CharField(max_length=200)
    order = models.IntegerField()

class LT_Films_Companies(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

class LT_Films_Countries(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

class LT_Films_Crew(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    credit_id = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    job = models.CharField(max_length=200)

class LT_Films_Genres(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('film', 'genre')

class LT_Films_Keywords(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    keyword = models.ForeignKey(Keyword, on_delete=models.DO_NOTHING)
    def get_absolute_url(self):
        return reverse('LT_Films_Keywords-detail', args=[str(self.id)])
    class Meta:
        unique_together = ('film', 'keyword')

class LT_Films_Languages(models.Model):
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

class LT_Viewer_Ratings(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.DO_NOTHING, null=True)
    film_a = models.ForeignKey(Film, on_delete=models.DO_NOTHING, related_name="film_a", null=True)
    film_b = models.ForeignKey(Film, on_delete=models.DO_NOTHING, related_name="film_b", null=True)
    date = models.DateField(default=date.today, null=True)
    a_points = models.DecimalField(decimal_places=1, max_digits=3, default=0, null=True)
    class Meta:
        unique_together = ('viewer', 'film_a', 'film_b')

class LT_Viewer_Seen(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.DO_NOTHING, null=True)
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING, null=True)
    seen_film = models.BooleanField(default=False, null=True)
    viewer_rating = models.DecimalField(decimal_places=8, max_digits=9, null=True)
    class Meta:
        indexes = [models.Index(fields=['viewer', 'film']),]

class LT_Viewer_Watchlist(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.DO_NOTHING)
    film = models.ForeignKey(Film, on_delete=models.DO_NOTHING)
    watchlist = models.BooleanField(default=False)
    class Meta:
        indexes = [models.Index(fields=['viewer', 'film']),]

class FriendRequest(models.Model):
    sender = models.ForeignKey(Viewer, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Viewer, related_name='received_requests', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def accept(self):
        """Accept the friend request and add to both users' friend lists."""
        self.status = 'accepted'
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()

    def reject(self):
        """Reject the friend request."""
        self.status = 'rejected'
        self.save()

    def __str__(self):
        return f"{self.sender.name} -> {self.receiver.name} ({self.status})"