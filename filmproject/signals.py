from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LT_Viewer_Seen, LT_Viewer_Watchlist, FeedEntry
from django.contrib.auth.models import User

import logging
logger = logging.getLogger(__name__)

@receiver(post_save, sender=LT_Viewer_Seen)
def create_seen_feed_entry(sender, instance, created, **kwargs):
    if  instance.seen_film:
        FeedEntry.objects.create(
            user=instance.viewer.user,
            movie=instance.film,
            action="marked as seen"
        )
        logger.info(f"Feed entry created for marking film as seen: {instance.film}")

@receiver(post_save, sender=LT_Viewer_Watchlist)
def create_watchlist_feed_entry(sender, instance, created, **kwargs):
    if  instance.watchlist:
        FeedEntry.objects.create(
            user=instance.viewer.user,
            movie=instance.film,
            action="added to watchlist"
        )
        logger.info(f"Feed entry created for adding film to watchlist: {instance.film}")
