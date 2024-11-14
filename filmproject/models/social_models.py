from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='profile_pictures/default_pfp.jpg')
    friends = models.ManyToManyField('self', blank=True)

    def has_seen_film(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, seen_film=True
        ).exists()

    def is_in_watchlist(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, watchlist=True
        ).exists()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile_viewer', args=[str(self.id)])

    def add_friend(self, viewer):
        if not self.is_friends_with(viewer):
            self.friends.add(viewer)
            self.save()

    def remove_friend(self, viewer):
        if self.is_friends_with(viewer):
            self.friends.remove(viewer)
            self.save()

    def is_friends_with(self, viewer):
        return self.friends.filter(id=viewer.id).exists()



class FriendRequest(models.Model):
    sender = models.ForeignKey('Viewer', related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey('Viewer', related_name='received_requests', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True)
    rejected_at = models.DateTimeField(null=True)

    def accept(self):
        self.status = 'accepted'
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()

    def reject(self):
        self.status = 'rejected'
        self.save()

    def __str__(self):
        return f"{self.sender.name} -> {self.receiver.name} ({self.status})"


class FeedEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('filmproject.Film', on_delete=models.CASCADE)  # Reference Film by string
    action = models.CharField(max_length=50)  # e.g., "added to watchlist" or "marked as seen"
    timestamp = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    feed_entry = models.ForeignKey('FeedEntry', related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    feed_entry = models.ForeignKey('FeedEntry', related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    TYPE_CHOICES = [
        ('like', 'Like'),
        ('comment', 'Comment'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    feed_entry = models.ForeignKey('FeedEntry', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.notification_type} on {self.feed_entry}"
