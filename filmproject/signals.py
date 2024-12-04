import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FeedEntry, LT_Viewer_Seen, LT_Viewer_Watchlist, User, Viewer


logger = logging.getLogger(__name__)

@receiver(post_save, sender=LT_Viewer_Seen)
def create_seen_feed_entry(sender, instance, created, **kwargs):
    if instance.seen_film:
        FeedEntry.objects.create(user=instance.viewer.user, movie=instance.film, action="marked as seen")
        logger.info(f"Feed entry created for marking film as seen: {instance.film}")


@receiver(post_save, sender=User)
def manage_viewer(sender, instance, created, **kwargs):
    if created:
        viewer, _ = Viewer.objects.get_or_create(user=instance)
        viewer.name = instance.username
        viewer.email = instance.email
        viewer.profile_picture =  instance.profile_picture
        viewer.save()


@receiver(post_save, sender=LT_Viewer_Watchlist)
def create_watchlist_feed_entry(sender, instance, created, **kwargs):
    if instance.watchlist:
        FeedEntry.objects.create(user=instance.viewer.user, movie=instance.film, action="added to watchlist")
        logger.info(f"Feed entry created for adding film to watchlist: {instance.film}")




