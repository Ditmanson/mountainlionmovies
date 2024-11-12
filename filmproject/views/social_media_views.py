import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from ..models import ( FeedEntry, Like, Comment, Notification)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from ..models import ( FeedEntry, Like, Comment, Notification)
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
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
            user=entry.user,
            feed_entry=entry,
            notification_type='like'
        )

    return JsonResponse({'success': True, 'likes': likes_count})


@login_required
@require_POST
def comment_entry(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)
    data = json.loads(request.body)
    comment = Comment.objects.create(feed_entry=entry, user=request.user, content=data['content'])

    # Create a notification if the entry is commented on by someone else
    if entry.user != request.user:
        Notification.objects.create(
            user=entry.user,
            feed_entry=entry,
            notification_type='comment'
        )

    return JsonResponse({'success': True, 'user': comment.user.username, 'content': comment.content})



def feed_page(request):
    return render(request, 'filmproject/social_feed.html')  # Adjust the path if necessary


def feed_entries(request):
    page = request.GET.get('page', 1)  # Get the page number from query params

    # Check if user has friends; handle if none
    user = request.user
    try:
        friends_viewers = user.viewer.friends.all()  # Assuming a 'friends' many-to-many relationship
        friends_users = [friend.user for friend in friends_viewers]  # Extract User instances
    except AttributeError:
        friends_users = []  # No friends attribute; proceed with an empty friends list

    # Get only actions from the user and their friends
    if friends_users:
        entries = FeedEntry.objects.filter(user__in=[user, *friends_users]).order_by('-timestamp')
    else:
        entries = FeedEntry.objects.filter(user=user).order_by('-timestamp')

    # Paginate the filtered entries
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_obj = paginator.get_page(page)

    # Prepare data for response
    data = [{
        'id': entry.id,
        'user': entry.user.username,
        'action': entry.action,
        'timestamp': entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        'likes': entry.likes.count(),
        'comments': [{'user': c.user.username, 'content': c.content} for c in entry.comments.all()],
        'movie': {
            'title': entry.movie.title,
            'tmdb_id': entry.movie.tmdb_id,
            'poster_path': entry.movie.poster_path
        }
    } for entry in page_obj]

    return JsonResponse(data, safe=False)


def feed_entry_detail(request, entry_id):
    entry = get_object_or_404(FeedEntry, id=entry_id)
    
    # Prepare data to render in the template
    data = {
        'id': entry.id,
        'user': entry.user.username,
        'action': entry.action,
        'timestamp': entry.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        'likes': entry.likes.count(),
        'comments': [{'user': c.user.username, 'content': c.content} for c in entry.comments.all()],
        'movie': {
            'title': entry.movie.title,
            'tmdb_id': entry.movie.tmdb_id,
            'poster_path': entry.movie.poster_path
        }
    }
    return render(request, 'filmproject/feed_entry_detail.html', {'entry': data})
