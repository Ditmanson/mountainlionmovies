
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
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        default="profile_pictures/default_pfp.jpg",
    )
    friends = models.ManyToManyField("self", blank=True)

    def xǁViewerǁhas_seen_film__mutmut_orig(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, seen_film=True
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_1(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=None, film=film, seen_film=True
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_2(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, film=None, seen_film=True
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_3(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, seen_film=False
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_4(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter( film=film, seen_film=True
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_5(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, seen_film=True
        ).exists()

    def xǁViewerǁhas_seen_film__mutmut_6(self, film):
        # Use string reference for LT_Viewer_Seen
        return self._meta.model._default_manager.filter(
            viewer=self, film=film,
        ).exists()

    xǁViewerǁhas_seen_film__mutmut_mutants = {
    'xǁViewerǁhas_seen_film__mutmut_1': xǁViewerǁhas_seen_film__mutmut_1, 
        'xǁViewerǁhas_seen_film__mutmut_2': xǁViewerǁhas_seen_film__mutmut_2, 
        'xǁViewerǁhas_seen_film__mutmut_3': xǁViewerǁhas_seen_film__mutmut_3, 
        'xǁViewerǁhas_seen_film__mutmut_4': xǁViewerǁhas_seen_film__mutmut_4, 
        'xǁViewerǁhas_seen_film__mutmut_5': xǁViewerǁhas_seen_film__mutmut_5, 
        'xǁViewerǁhas_seen_film__mutmut_6': xǁViewerǁhas_seen_film__mutmut_6
    }

    def has_seen_film(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁhas_seen_film__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁhas_seen_film__mutmut_mutants"), *args, **kwargs)
        return result 

    has_seen_film.__signature__ = _mutmut_signature(xǁViewerǁhas_seen_film__mutmut_orig)
    xǁViewerǁhas_seen_film__mutmut_orig.__name__ = 'xǁViewerǁhas_seen_film'



    def xǁViewerǁis_in_watchlist__mutmut_orig(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, watchlist=True
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_1(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=None, film=film, watchlist=True
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_2(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, film=None, watchlist=True
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_3(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, film=film, watchlist=False
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_4(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter( film=film, watchlist=True
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_5(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, watchlist=True
        ).exists()

    def xǁViewerǁis_in_watchlist__mutmut_6(self, film):
        # Use string reference for LT_Viewer_Watchlist
        return self._meta.model._default_manager.filter(
            viewer=self, film=film,
        ).exists()

    xǁViewerǁis_in_watchlist__mutmut_mutants = {
    'xǁViewerǁis_in_watchlist__mutmut_1': xǁViewerǁis_in_watchlist__mutmut_1, 
        'xǁViewerǁis_in_watchlist__mutmut_2': xǁViewerǁis_in_watchlist__mutmut_2, 
        'xǁViewerǁis_in_watchlist__mutmut_3': xǁViewerǁis_in_watchlist__mutmut_3, 
        'xǁViewerǁis_in_watchlist__mutmut_4': xǁViewerǁis_in_watchlist__mutmut_4, 
        'xǁViewerǁis_in_watchlist__mutmut_5': xǁViewerǁis_in_watchlist__mutmut_5, 
        'xǁViewerǁis_in_watchlist__mutmut_6': xǁViewerǁis_in_watchlist__mutmut_6
    }

    def is_in_watchlist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁis_in_watchlist__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁis_in_watchlist__mutmut_mutants"), *args, **kwargs)
        return result 

    is_in_watchlist.__signature__ = _mutmut_signature(xǁViewerǁis_in_watchlist__mutmut_orig)
    xǁViewerǁis_in_watchlist__mutmut_orig.__name__ = 'xǁViewerǁis_in_watchlist'



    def xǁViewerǁ__str____mutmut_orig(self):
        return self.name

    xǁViewerǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁViewerǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁViewerǁ__str____mutmut_orig)
    xǁViewerǁ__str____mutmut_orig.__name__ = 'xǁViewerǁ__str__'



    def xǁViewerǁget_absolute_url__mutmut_orig(self):
        return reverse("profile_viewer", args=[str(self.id)])

    def xǁViewerǁget_absolute_url__mutmut_1(self):
        return reverse("XXprofile_viewerXX", args=[str(self.id)])

    def xǁViewerǁget_absolute_url__mutmut_2(self):
        return reverse("profile_viewer",)

    xǁViewerǁget_absolute_url__mutmut_mutants = {
    'xǁViewerǁget_absolute_url__mutmut_1': xǁViewerǁget_absolute_url__mutmut_1, 
        'xǁViewerǁget_absolute_url__mutmut_2': xǁViewerǁget_absolute_url__mutmut_2
    }

    def get_absolute_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁget_absolute_url__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁget_absolute_url__mutmut_mutants"), *args, **kwargs)
        return result 

    get_absolute_url.__signature__ = _mutmut_signature(xǁViewerǁget_absolute_url__mutmut_orig)
    xǁViewerǁget_absolute_url__mutmut_orig.__name__ = 'xǁViewerǁget_absolute_url'



    def xǁViewerǁadd_friend__mutmut_orig(self, viewer):
        if not self.is_friends_with(viewer):
            self.friends.add(viewer)
            self.save()

    def xǁViewerǁadd_friend__mutmut_1(self, viewer):
        if  self.is_friends_with(viewer):
            self.friends.add(viewer)
            self.save()

    def xǁViewerǁadd_friend__mutmut_2(self, viewer):
        if not self.is_friends_with(None):
            self.friends.add(viewer)
            self.save()

    def xǁViewerǁadd_friend__mutmut_3(self, viewer):
        if not self.is_friends_with(viewer):
            self.friends.add(None)
            self.save()

    xǁViewerǁadd_friend__mutmut_mutants = {
    'xǁViewerǁadd_friend__mutmut_1': xǁViewerǁadd_friend__mutmut_1, 
        'xǁViewerǁadd_friend__mutmut_2': xǁViewerǁadd_friend__mutmut_2, 
        'xǁViewerǁadd_friend__mutmut_3': xǁViewerǁadd_friend__mutmut_3
    }

    def add_friend(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁadd_friend__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁadd_friend__mutmut_mutants"), *args, **kwargs)
        return result 

    add_friend.__signature__ = _mutmut_signature(xǁViewerǁadd_friend__mutmut_orig)
    xǁViewerǁadd_friend__mutmut_orig.__name__ = 'xǁViewerǁadd_friend'



    def xǁViewerǁremove_friend__mutmut_orig(self, viewer):
        if self.is_friends_with(viewer):
            self.friends.remove(viewer)
            self.save()

    def xǁViewerǁremove_friend__mutmut_1(self, viewer):
        if self.is_friends_with(None):
            self.friends.remove(viewer)
            self.save()

    def xǁViewerǁremove_friend__mutmut_2(self, viewer):
        if self.is_friends_with(viewer):
            self.friends.remove(None)
            self.save()

    xǁViewerǁremove_friend__mutmut_mutants = {
    'xǁViewerǁremove_friend__mutmut_1': xǁViewerǁremove_friend__mutmut_1, 
        'xǁViewerǁremove_friend__mutmut_2': xǁViewerǁremove_friend__mutmut_2
    }

    def remove_friend(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁremove_friend__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁremove_friend__mutmut_mutants"), *args, **kwargs)
        return result 

    remove_friend.__signature__ = _mutmut_signature(xǁViewerǁremove_friend__mutmut_orig)
    xǁViewerǁremove_friend__mutmut_orig.__name__ = 'xǁViewerǁremove_friend'



    def xǁViewerǁis_friends_with__mutmut_orig(self, viewer):
        return self.friends.filter(id=viewer.id).exists()

    xǁViewerǁis_friends_with__mutmut_mutants = {

    }

    def is_friends_with(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerǁis_friends_with__mutmut_orig"), object.__getattribute__(self, "xǁViewerǁis_friends_with__mutmut_mutants"), *args, **kwargs)
        return result 

    is_friends_with.__signature__ = _mutmut_signature(xǁViewerǁis_friends_with__mutmut_orig)
    xǁViewerǁis_friends_with__mutmut_orig.__name__ = 'xǁViewerǁis_friends_with'




class FriendRequest(models.Model):
    sender = models.ForeignKey(
        "Viewer", related_name="sent_requests", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        "Viewer", related_name="received_requests", on_delete=models.CASCADE
    )
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True)
    rejected_at = models.DateTimeField(null=True)

    def xǁFriendRequestǁaccept__mutmut_orig(self):
        self.status = "accepted"
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()

    def xǁFriendRequestǁaccept__mutmut_1(self):
        self.status = "XXacceptedXX"
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()

    def xǁFriendRequestǁaccept__mutmut_2(self):
        self.status = None
        self.sender.add_friend(self.receiver)
        self.receiver.add_friend(self.sender)
        self.save()

    xǁFriendRequestǁaccept__mutmut_mutants = {
    'xǁFriendRequestǁaccept__mutmut_1': xǁFriendRequestǁaccept__mutmut_1, 
        'xǁFriendRequestǁaccept__mutmut_2': xǁFriendRequestǁaccept__mutmut_2
    }

    def accept(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFriendRequestǁaccept__mutmut_orig"), object.__getattribute__(self, "xǁFriendRequestǁaccept__mutmut_mutants"), *args, **kwargs)
        return result 

    accept.__signature__ = _mutmut_signature(xǁFriendRequestǁaccept__mutmut_orig)
    xǁFriendRequestǁaccept__mutmut_orig.__name__ = 'xǁFriendRequestǁaccept'



    def xǁFriendRequestǁreject__mutmut_orig(self):
        self.status = "rejected"
        self.save()

    def xǁFriendRequestǁreject__mutmut_1(self):
        self.status = "XXrejectedXX"
        self.save()

    def xǁFriendRequestǁreject__mutmut_2(self):
        self.status = None
        self.save()

    xǁFriendRequestǁreject__mutmut_mutants = {
    'xǁFriendRequestǁreject__mutmut_1': xǁFriendRequestǁreject__mutmut_1, 
        'xǁFriendRequestǁreject__mutmut_2': xǁFriendRequestǁreject__mutmut_2
    }

    def reject(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFriendRequestǁreject__mutmut_orig"), object.__getattribute__(self, "xǁFriendRequestǁreject__mutmut_mutants"), *args, **kwargs)
        return result 

    reject.__signature__ = _mutmut_signature(xǁFriendRequestǁreject__mutmut_orig)
    xǁFriendRequestǁreject__mutmut_orig.__name__ = 'xǁFriendRequestǁreject'



    def xǁFriendRequestǁ__str____mutmut_orig(self):
        return f"{self.sender.name} -> {self.receiver.name} ({self.status})"

    xǁFriendRequestǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFriendRequestǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁFriendRequestǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁFriendRequestǁ__str____mutmut_orig)
    xǁFriendRequestǁ__str____mutmut_orig.__name__ = 'xǁFriendRequestǁ__str__'




class FeedEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        "filmproject.Film", on_delete=models.CASCADE
    )  # Reference Film by string
    # e.g., "added to watchlist" or "marked as seen"
    action = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    feed_entry = models.ForeignKey(
        "FeedEntry", related_name="likes", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    feed_entry = models.ForeignKey(
        "FeedEntry", related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    TYPE_CHOICES = [
        ("like", "Like"),
        ("comment", "Comment"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    feed_entry = models.ForeignKey("FeedEntry", on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def xǁNotificationǁ__str____mutmut_orig(self):
        return f"{self.user.username} - {self.notification_type} on {self.feed_entry}"

    xǁNotificationǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁNotificationǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁNotificationǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁNotificationǁ__str____mutmut_orig)
    xǁNotificationǁ__str____mutmut_orig.__name__ = 'xǁNotificationǁ__str__'


