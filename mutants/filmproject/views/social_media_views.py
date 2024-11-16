
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


import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from ..models import FeedEntry, Like, Comment, Notification
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.paginator import Paginator


@login_required
@require_POST
def like_entry(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)
    Like.objects.get_or_create(feed_entry=entry, user=request.user)
    likes_count = entry.likes.count()

    # Create a notification if the entry is liked by someone else
    if entry.user != request.user:
        Notification.objects.create(
            user=entry.user, feed_entry=entry, notification_type="like"
        )

    return JsonResponse({"success": True, "likes": likes_count})


@login_required
@require_POST
def comment_entry(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)
    data = json.loads(request.body)
    comment = Comment.objects.create(
        feed_entry=entry, user=request.user, content=data["content"]
    )

    # Create a notification if the entry is commented on by someone else
    if entry.user != request.user:
        Notification.objects.create(
            user=entry.user, feed_entry=entry, notification_type="comment"
        )

    return JsonResponse(
        {
            "success": True,
            "user": comment.user.username,
            "content": comment.content,
        }
    )


def x_feed_page__mutmut_orig(request):
    # Adjust the path if necessary
    return render(request, "filmproject/social_feed.html")


def x_feed_page__mutmut_1(request):
    # Adjust the path if necessary
    return render(None, "filmproject/social_feed.html")


def x_feed_page__mutmut_2(request):
    # Adjust the path if necessary
    return render(request, "XXfilmproject/social_feed.htmlXX")


def x_feed_page__mutmut_3(request):
    # Adjust the path if necessary
    return render( "filmproject/social_feed.html")

x_feed_page__mutmut_mutants = {
'x_feed_page__mutmut_1': x_feed_page__mutmut_1, 
    'x_feed_page__mutmut_2': x_feed_page__mutmut_2, 
    'x_feed_page__mutmut_3': x_feed_page__mutmut_3
}

def feed_page(*args, **kwargs):
    result = _mutmut_trampoline(x_feed_page__mutmut_orig, x_feed_page__mutmut_mutants, *args, **kwargs)
    return result 

feed_page.__signature__ = _mutmut_signature(x_feed_page__mutmut_orig)
x_feed_page__mutmut_orig.__name__ = 'x_feed_page'




def x_feed_entries__mutmut_orig(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_1(request):
    page = request.GET.get("XXpageXX", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_2(request):
    page = request.GET.get("page", 2)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_3(request):
    page = None  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_4(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = None
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_5(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = None
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_6(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = None
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_7(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = None  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_8(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("XX-timestampXX")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_9(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = None
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_10(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=None).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_11(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("XX-timestampXX")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_12(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = None

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_13(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(None, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_14(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 11)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_15(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator( 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_16(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = None  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_17(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(None)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_18(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = None

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_19(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "XXidXX": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_20(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "XXuserXX": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_21(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "XXactionXX": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_22(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "XXtimestampXX": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_23(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("XX%Y-%m-%d %H:%M:%SXX"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_24(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "XXlikesXX": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_25(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "XXcommentsXX": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_26(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"XXuserXX": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_27(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "XXcontentXX": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_28(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "XXmovieXX": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_29(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "XXtitleXX": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_30(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "XXtmdb_idXX": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_31(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "XXposter_pathXX": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_32(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = None

    return JsonResponse(data, safe=False)


def x_feed_entries__mutmut_33(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(None, safe=False)


def x_feed_entries__mutmut_34(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data, safe=True)


def x_feed_entries__mutmut_35(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse( safe=False)


def x_feed_entries__mutmut_36(request):
    page = request.GET.get("page", 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        # Assuming a 'friends' many-to-many relationship
        friends_viewers = user.viewer.friends.all()
        # Extract User instances
        friends_users = [friend.user for friend in friends_viewers]
    except AttributeError:
        friends_users = (
            []
        )  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(
            user__in=[user, *friends_users]
        ).order_by("-timestamp")
    else:
        entries = FeedEntry.objects.filter(user=user).order_by("-timestamp")

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [
        {
            "id": entry.id,
            "user": entry.user.username,
            "action": entry.action,
            "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "likes": entry.likes.count(),
            "comments": [
                {"user": c.user.username, "content": c.content}
                for c in entry.comments.all()
            ],
            "movie": {
                "title": entry.movie.title,
                "tmdb_id": entry.movie.tmdb_id,
                "poster_path": entry.movie.poster_path,
            },
        }
        for entry in page_obj
    ]

    return JsonResponse(data,)

x_feed_entries__mutmut_mutants = {
'x_feed_entries__mutmut_1': x_feed_entries__mutmut_1, 
    'x_feed_entries__mutmut_2': x_feed_entries__mutmut_2, 
    'x_feed_entries__mutmut_3': x_feed_entries__mutmut_3, 
    'x_feed_entries__mutmut_4': x_feed_entries__mutmut_4, 
    'x_feed_entries__mutmut_5': x_feed_entries__mutmut_5, 
    'x_feed_entries__mutmut_6': x_feed_entries__mutmut_6, 
    'x_feed_entries__mutmut_7': x_feed_entries__mutmut_7, 
    'x_feed_entries__mutmut_8': x_feed_entries__mutmut_8, 
    'x_feed_entries__mutmut_9': x_feed_entries__mutmut_9, 
    'x_feed_entries__mutmut_10': x_feed_entries__mutmut_10, 
    'x_feed_entries__mutmut_11': x_feed_entries__mutmut_11, 
    'x_feed_entries__mutmut_12': x_feed_entries__mutmut_12, 
    'x_feed_entries__mutmut_13': x_feed_entries__mutmut_13, 
    'x_feed_entries__mutmut_14': x_feed_entries__mutmut_14, 
    'x_feed_entries__mutmut_15': x_feed_entries__mutmut_15, 
    'x_feed_entries__mutmut_16': x_feed_entries__mutmut_16, 
    'x_feed_entries__mutmut_17': x_feed_entries__mutmut_17, 
    'x_feed_entries__mutmut_18': x_feed_entries__mutmut_18, 
    'x_feed_entries__mutmut_19': x_feed_entries__mutmut_19, 
    'x_feed_entries__mutmut_20': x_feed_entries__mutmut_20, 
    'x_feed_entries__mutmut_21': x_feed_entries__mutmut_21, 
    'x_feed_entries__mutmut_22': x_feed_entries__mutmut_22, 
    'x_feed_entries__mutmut_23': x_feed_entries__mutmut_23, 
    'x_feed_entries__mutmut_24': x_feed_entries__mutmut_24, 
    'x_feed_entries__mutmut_25': x_feed_entries__mutmut_25, 
    'x_feed_entries__mutmut_26': x_feed_entries__mutmut_26, 
    'x_feed_entries__mutmut_27': x_feed_entries__mutmut_27, 
    'x_feed_entries__mutmut_28': x_feed_entries__mutmut_28, 
    'x_feed_entries__mutmut_29': x_feed_entries__mutmut_29, 
    'x_feed_entries__mutmut_30': x_feed_entries__mutmut_30, 
    'x_feed_entries__mutmut_31': x_feed_entries__mutmut_31, 
    'x_feed_entries__mutmut_32': x_feed_entries__mutmut_32, 
    'x_feed_entries__mutmut_33': x_feed_entries__mutmut_33, 
    'x_feed_entries__mutmut_34': x_feed_entries__mutmut_34, 
    'x_feed_entries__mutmut_35': x_feed_entries__mutmut_35, 
    'x_feed_entries__mutmut_36': x_feed_entries__mutmut_36
}

def feed_entries(*args, **kwargs):
    result = _mutmut_trampoline(x_feed_entries__mutmut_orig, x_feed_entries__mutmut_mutants, *args, **kwargs)
    return result 

feed_entries.__signature__ = _mutmut_signature(x_feed_entries__mutmut_orig)
x_feed_entries__mutmut_orig.__name__ = 'x_feed_entries'




def x_feed_entry_detail__mutmut_orig(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_1(request, entry_id):
    entry = get_object_or_404(None, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_2(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=None)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_3(request, entry_id):
    entry = get_object_or_404( id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_4(request, entry_id):
    entry = get_object_or_404(FeedEntry,)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_5(request, entry_id):
    entry = None

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_6(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "XXidXX": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_7(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "XXuserXX": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_8(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "XXactionXX": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_9(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "XXtimestampXX": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_10(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("XX%Y-%m-%d %H:%M:%SXX"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_11(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "XXlikesXX": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_12(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "XXcommentsXX": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_13(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"XXuserXX": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_14(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "XXcontentXX": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_15(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "XXmovieXX": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_16(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "XXtitleXX": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_17(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "XXtmdb_idXX": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_18(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "XXposter_pathXX": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_19(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = None
    return render(
        request, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_20(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        None, "filmproject/feed_entry_detail.html", {"entry": data}
    )


def x_feed_entry_detail__mutmut_21(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "XXfilmproject/feed_entry_detail.htmlXX", {"entry": data}
    )


def x_feed_entry_detail__mutmut_22(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render(
        request, "filmproject/feed_entry_detail.html", {"XXentryXX": data}
    )


def x_feed_entry_detail__mutmut_23(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)

    # Prepare data to render in the template
    data = {
        "id": entry.id,
        "user": entry.user.username,
        "action": entry.action,
        "timestamp": entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "likes": entry.likes.count(),
        "comments": [
            {"user": c.user.username, "content": c.content}
            for c in entry.comments.all()
        ],
        "movie": {
            "title": entry.movie.title,
            "tmdb_id": entry.movie.tmdb_id,
            "poster_path": entry.movie.poster_path,
        },
    }
    return render( "filmproject/feed_entry_detail.html", {"entry": data}
    )

x_feed_entry_detail__mutmut_mutants = {
'x_feed_entry_detail__mutmut_1': x_feed_entry_detail__mutmut_1, 
    'x_feed_entry_detail__mutmut_2': x_feed_entry_detail__mutmut_2, 
    'x_feed_entry_detail__mutmut_3': x_feed_entry_detail__mutmut_3, 
    'x_feed_entry_detail__mutmut_4': x_feed_entry_detail__mutmut_4, 
    'x_feed_entry_detail__mutmut_5': x_feed_entry_detail__mutmut_5, 
    'x_feed_entry_detail__mutmut_6': x_feed_entry_detail__mutmut_6, 
    'x_feed_entry_detail__mutmut_7': x_feed_entry_detail__mutmut_7, 
    'x_feed_entry_detail__mutmut_8': x_feed_entry_detail__mutmut_8, 
    'x_feed_entry_detail__mutmut_9': x_feed_entry_detail__mutmut_9, 
    'x_feed_entry_detail__mutmut_10': x_feed_entry_detail__mutmut_10, 
    'x_feed_entry_detail__mutmut_11': x_feed_entry_detail__mutmut_11, 
    'x_feed_entry_detail__mutmut_12': x_feed_entry_detail__mutmut_12, 
    'x_feed_entry_detail__mutmut_13': x_feed_entry_detail__mutmut_13, 
    'x_feed_entry_detail__mutmut_14': x_feed_entry_detail__mutmut_14, 
    'x_feed_entry_detail__mutmut_15': x_feed_entry_detail__mutmut_15, 
    'x_feed_entry_detail__mutmut_16': x_feed_entry_detail__mutmut_16, 
    'x_feed_entry_detail__mutmut_17': x_feed_entry_detail__mutmut_17, 
    'x_feed_entry_detail__mutmut_18': x_feed_entry_detail__mutmut_18, 
    'x_feed_entry_detail__mutmut_19': x_feed_entry_detail__mutmut_19, 
    'x_feed_entry_detail__mutmut_20': x_feed_entry_detail__mutmut_20, 
    'x_feed_entry_detail__mutmut_21': x_feed_entry_detail__mutmut_21, 
    'x_feed_entry_detail__mutmut_22': x_feed_entry_detail__mutmut_22, 
    'x_feed_entry_detail__mutmut_23': x_feed_entry_detail__mutmut_23
}

def feed_entry_detail(*args, **kwargs):
    result = _mutmut_trampoline(x_feed_entry_detail__mutmut_orig, x_feed_entry_detail__mutmut_mutants, *args, **kwargs)
    return result 

feed_entry_detail.__signature__ = _mutmut_signature(x_feed_entry_detail__mutmut_orig)
x_feed_entry_detail__mutmut_orig.__name__ = 'x_feed_entry_detail'


