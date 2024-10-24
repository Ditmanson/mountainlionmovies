
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import IntegrityError
from django.db import models
from django.db.models import F, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from ..forms import ViewerRegistrationForm
from ..models import (Viewer, LT_Viewer_Ratings, LT_Viewer_Seen,
                       LT_Viewer_Watchlist, FriendRequest, Film)
from ..tokens import account_activation_token
from django.contrib import messages


class ViewerDetailView(generic.DetailView):
    model = Viewer

    def get(self, request, *args, **kwargs):
        viewer = self.get_object()
        return redirect('profile_viewer', viewer_id=viewer.id)


class ViewerListView(generic.ListView):
    model = Viewer


@login_required
def profile(request, viewer_id=None):
    user = request.user
    try:
        # Get the viewer based on the ID passed or the current user
        if viewer_id:
            viewer = get_object_or_404(Viewer, id=viewer_id)
        else:
            viewer = user.viewer
    except Viewer.DoesNotExist:
        # Handle the case where the viewer doesn't exist yet
        if Viewer.objects.filter(email=user.email).exists():
            viewer = Viewer.objects.get(email=user.email)
        else:
            try:
                viewer = Viewer.objects.create(user=user, name=user.username, email=user.email)
            except IntegrityError:
                return render(request, 'filmproject/profile_error.html', {'error': 'Email conflict, unable to create viewer.'})

    # Friend request logic
    friend_request = None
    received_friend_request = None
    if request.user.viewer != viewer:
        # Outgoing friend request
        friend_request = FriendRequest.objects.filter(sender=request.user.viewer, receiver=viewer).first()
        # Incoming friend request
        received_friend_request = FriendRequest.objects.filter(sender=viewer, receiver=request.user.viewer, status='pending').first()

    
    # Get films in the viewer's watchlist
    watchlist = Film.objects.filter(lt_viewer_watchlist__viewer=viewer, lt_viewer_watchlist__watchlist=True)
    # Fetch all films the viewer has seen
    seen_films = Film.objects.filter(lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True)
    # Calculate the dynamic rating for each film
    film_ratings = []
    for film in seen_films:
        # Get total points for the film as film_a
        a_points_sum = LT_Viewer_Ratings.objects.filter(film_a=film, viewer=viewer).aggregate(
            total_a_points=Sum('a_points')
        )['total_a_points'] or 0
        # Get total points for the film as film_b
        b_points_sum = LT_Viewer_Ratings.objects.filter(film_b=film, viewer=viewer).aggregate(
            total_b_points=Sum(F('a_points') * -1 + 1)
        )['total_b_points'] or 0
        # Count total comparisons involving this film
        total_count = LT_Viewer_Ratings.objects.filter(
            models.Q(film_a=film) | models.Q(film_b=film), viewer=viewer
        ).count()
        # Calculate the user rating dynamically
        user_rating = (a_points_sum + b_points_sum) / total_count if total_count > 0 else 0
        # Add to film ratings list
        film_ratings.append({
            'film': film,
            'user_rating': user_rating
        })
    # Sort the films by rating in descending order
    film_ratings.sort(key=lambda x: x['user_rating'], reverse=True)
   
    # Sort the films by rating in descending order
    film_ratings.sort(key=lambda x: x['user_rating'], reverse=True)

    # In your profile view
    top_ten_films = film_ratings[:10]  # Top 10 user-rated films
    remaining_seen_films = film_ratings[10:]  # All others

    # Add the necessary context for the template
    context = {
        'viewer': viewer,
        'watchlist': watchlist,  # Include the watchlist
        'seen_films': film_ratings,  # Include the seen films
        'top_ten_films': top_ten_films,  # Add top ten films to context
        'remaining_seen_films': remaining_seen_films,  # Add remaining films to context
        'friend_request': friend_request,
        'received_friend_request': received_friend_request,
        
        'num_pending_requests': FriendRequest.objects.filter(receiver=user.viewer, status='pending').count(),
    }

    return render(request, 'filmproject/profile.html', context)




def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'filmproject/account_activation_invalid.html')
    

def register(request):
    if request.method == 'POST':
        form = ViewerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            print("\nREQUEST POST:", request.POST,"\n")
            print("\nREQUEST FILES", request.FILES,"\n")
            print("\nUSER FORM", user,"\n")
            user.is_active = False  # Deactivate account until email verification
            user.save()

            # Create the Viewer object linked to the user
            Viewer.objects.create(user=user, name=user.username, email=user.email, profile_picture=user.profile_picture)

            # Send activation email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('filmproject/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, 'mountainlionmovies@gmail.com', [to_email])  

            return render(request, 'filmproject/registration_confirm.html')
    else:
        form = ViewerRegistrationForm()
    return render(request, 'filmproject/register.html', {'form': form})


@login_required
def send_friend_request(request, viewer_id):
    """Send a friend request to another viewer."""
    receiver = get_object_or_404(Viewer, id=viewer_id)
    
    # Check if a pending friend request already exists
    if FriendRequest.objects.filter(sender=request.user.viewer, receiver=receiver, status='pending').exists():
        messages.info(request, 'Friend request already sent.')
    else:
        # Create a new friend request
        FriendRequest.objects.create(sender=request.user.viewer, receiver=receiver)
        messages.success(request, f'Friend request sent to {receiver.name}.')
    
    # Redirect to the receiver's profile after sending the friend request
    return redirect('profile_viewer', viewer_id=receiver.id)


@login_required
def accept_friend_request(request, request_id):
    """Accept a friend request."""
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    
    if friend_request.status == 'pending':
        friend_request.accept()  # Custom method to handle acceptance
        messages.success(request, f'You are now friends with {friend_request.sender.name}.')
        
        # Redirect to the sender's profile after accepting the friend request
        return redirect('profile_viewer', viewer_id=friend_request.sender.id)
    
    messages.error(request, 'Invalid request.')
    return redirect('profile', viewer_id=request.user.viewer.id)  # Redirect to the current user's profile



@login_required
def reject_friend_request(request, request_id):
    """Reject a friend request."""
    friend_request = get_object_or_404(FriendRequest, id=request_id, receiver=request.user.viewer)
    
    # Ensure the request is pending before rejecting
    if friend_request.status == 'pending':
        friend_request.reject()  # Custom method to handle rejection
        messages.success(request, f'Friend request from {friend_request.sender.name} rejected.')
        return redirect('profile', viewer_id=friend_request.sender.id)
    
    messages.error(request, 'Invalid request.')
    return redirect('profile', viewer_id=request.user.viewer.id)


@login_required
def remove_friend(request, viewer_id):
    """Remove a friend from the user's friend list."""
    viewer_to_remove = get_object_or_404(Viewer, id=viewer_id)
    viewer = request.user.viewer  # Get the current user's viewer object
    
    # Remove the friend connection bidirectionally
    viewer.friends.remove(viewer_to_remove)
    viewer_to_remove.friends.remove(viewer)
    
    messages.success(request, f'{viewer_to_remove.name} has been removed from your friend list.')
    
    return redirect('profile', viewer_id=request.user.viewer.id)  # Redirect back to the user's profile


@login_required
def manage_friend_requests(request):
    """Display the user's friend requests (both sent and received)."""
    user_viewer = request.user.viewer
    
    # Retrieve received and sent friend requests
    received_friend_requests = FriendRequest.objects.filter(receiver=user_viewer, status='pending')
    sent_friend_requests = FriendRequest.objects.filter(sender=user_viewer)

    context = {
        'received_friend_requests': received_friend_requests,
        'sent_friend_requests': sent_friend_requests,
    }
    
    return render(request, 'filmproject/friend_requests.html', context)


def base_context_processor(request):

    if request.user.is_authenticated:
        num_pending_requests = FriendRequest.objects.filter(receiver=request.user.viewer, status='pending').count()
    else:
        num_pending_requests = 0
    return {'num_pending_requests': num_pending_requests}

def viewer_list(request):
    viewers = Viewer.objects.all()
    return render(request, 'filmproject/viewer_list.html', {'viewer_list': viewers})

