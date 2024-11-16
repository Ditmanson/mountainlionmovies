
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


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LT_Viewer_Seen, LT_Viewer_Watchlist, FeedEntry

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=LT_Viewer_Seen)
def create_seen_feed_entry(sender, instance, created, **kwargs):
    if instance.seen_film:
        FeedEntry.objects.create(
            user=instance.viewer.user,
            movie=instance.film,
            action="marked as seen",
        )
        logger.info(
            f"Feed entry created for marking film as seen: {instance.film}"
        )


@receiver(post_save, sender=LT_Viewer_Watchlist)
def create_watchlist_feed_entry(sender, instance, created, **kwargs):
    if instance.watchlist:
        FeedEntry.objects.create(
            user=instance.viewer.user,
            movie=instance.film,
            action="added to watchlist",
        )
        logger.info(
            f"Feed entry created for adding film to watchlist: {instance.film}"
        )


# @receiver(post_save, sender=LT_Viewer_Seen)
# def update_film_mlm_rating_on_save(sender, instance, **kwargs):
#     # Signal handler to update mlm_rating of the film
#     # when a viewer rating is saved
#     instance.film.update_mlm_rating()
#     logger.info(f"Updated mlm_rating for film: {instance.film.title}")


# @receiver(post_delete, sender=LT_Viewer_Seen)
# def update_film_mlm_rating_on_delete(sender, instance, **kwargs):
#     # Signal handler to update mlm_rating of the film
#     # when a viewer rating is deleted
#     instance.film.update_mlm_rating()
#     logger.info(
#         f"Updated mlm_rating for film after deletion: {instance.film.title}"
#     )
