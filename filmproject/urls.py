from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.api_views import (
    FilmViewSet,
    FriendRequestViewSet,
    LT_Viewer_WatchlistViewSet,
    LT_Viewer_SeenViewSet,
    LT_Films_CastViewSet,
    LT_Films_CompaniesViewSet,
    LT_Films_CountriesViewSet,
    LT_Films_CrewViewSet,
    LT_Films_GenresViewSet,
    LT_Films_KeywordsViewSet,
    LT_Films_LanguagesViewSet,
    LT_Viewer_RatingsViewSet,
    NotificationsViewSet,
    PersonViewSet,
    user_watchlist,
    user_seen_films,
    ViewerViewSet,
)

from .views.film_views import (
    add_to_watchlist,
    FilmListView,
    FilmDetailView,
    index,
    mark_as_seen,
    remove_from_seen,
    remove_from_watchlist,
    search_movies,
)

from .views.profile_views import (
    accept_friend_request,
    activate,
    ProfileView,
    register,
    reject_friend_request,
    remove_friend,
    render_invalid_activation_page,
    resend_activation_email,
    search_results,
    send_friend_request,
    update_profile,
    ViewerListView,
)

from .views.rating_views import (
    compare_movies,
    submit_movie_selection,
)

from .views.social_media_views import (
    comment_entry,
    feed_entries,
    feed_entry_detail,
    feed_page,
    like_entry,
)

from .views.staff_views import (
    manual_update_film_ratings,
    manual_calculate_cosine_similarity,
    manual_database_cleanup,
    staff_dashboard,
)

# Create a router and register all the viewsets
router = DefaultRouter()
router.register(r"films", FilmViewSet)
router.register(r"people", PersonViewSet)
router.register(r"viewers", ViewerViewSet)
router.register(r"watchlist", LT_Viewer_WatchlistViewSet)
router.register(r"seen_films", LT_Viewer_SeenViewSet)
router.register(r"friend_requests", FriendRequestViewSet)
router.register(r"film_cast", LT_Films_CastViewSet)
router.register(r"film_companies", LT_Films_CompaniesViewSet)
router.register(r"film_countries", LT_Films_CountriesViewSet)
router.register(r"film_crew", LT_Films_CrewViewSet)
router.register(r"film_genres", LT_Films_GenresViewSet)
router.register(r"film_keywords", LT_Films_KeywordsViewSet)
router.register(r"film_languages", LT_Films_LanguagesViewSet)
router.register(r"viewer_ratings", LT_Viewer_RatingsViewSet)
router.register(r"notifications", NotificationsViewSet)

urlpatterns = [
    # Authentication-related URLs
    path("login/", auth_views.LoginView.as_view(template_name="filmproject/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="filmproject/index.html"), name="logout"),
    path("register/", register, name="register"),
    path("resend-activation/<str:uidb64>/", resend_activation_email, name="resend_activation"),

    # Email activation
    path("activate/<uidb64>/<token>/", activate, name="activate"),

    # Film-related URLs
    path("films/", FilmListView.as_view(), name="film_list"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film-detail"),
    path("films/<int:pk>/add_to_watchlist/", add_to_watchlist, name="add_to_watchlist"),
    path("films/<int:pk>/mark_as_seen/", mark_as_seen, name="mark_as_seen"),
    path("films/<int:pk>/remove_from_seen/", remove_from_seen, name="remove_from_seen"),
    path("films/<int:pk>/remove_from_watchlist/", remove_from_watchlist, name="remove_from_watchlist"),

    # Friend request URLs
    path("send_friend_request/<int:viewer_id>/", send_friend_request, name="send_friend_request"),
    path("accept_friend_request/<int:request_id>/", accept_friend_request, name="accept_friend_request"),
    path("reject_friend_request/<int:request_id>/", reject_friend_request, name="reject_friend_request"),
    path("remove_friend/<int:viewer_id>/", remove_friend, name="remove_friend"),

    # Home page
    path("", index, name="index"),
    path("index", index, name="index"),

    # Invalid activation page URL
    path("activation/invalid/", render_invalid_activation_page, name="invalid_activation"),

    # Movie search and popular movies
    path("search_movies/", search_movies, name="search_movies"),

    # Navbar Search
    path("search_results/", search_results, name="search_results"),

    # Password reset URLs
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="filmproject/password_reset.html"), name="password_reset"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="filmproject/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="filmproject/password_reset_done.html"), name="password_reset_done"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="filmproject/password_reset_complete.html"), name="password_reset_complete"),

    # Profile pages
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("profile/<int:viewer_id>/", ProfileView.as_view(), name="profile_viewer"),
    path("update_profile/<int:pk>/", update_profile, name="update_profile"),

    # Ratings-related URLs
    path("compare_movies/", compare_movies, name="compare_movies"),
    path("compare_movies/submit_selection/", submit_movie_selection, name="submit_movie_selection"),

    # Social feed URLs
    path("feed/", feed_page, name="feed_page"),
    path("feed_entries/", feed_entries, name="feed_entries"),
    path("like_entry/<int:entry_id>/", like_entry, name="like_entry"),
    path("comment_entry/<int:entry_id>/", comment_entry, name="comment_entry"),
    path("feed_entry/<int:entry_id>/", feed_entry_detail, name="feed_entry_detail"),

    # Staff Superpower URLs
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    path('super/update-film-ratings/', manual_update_film_ratings, name='manual_update_film_ratings'),
    path('super/calculate-cosine-similarity/', manual_calculate_cosine_similarity, name='manual_calculate_cosine_similarity'),
    path('super/database-cleanup/', manual_database_cleanup, name='manual_database_cleanup'),

    # Viewer list
    path("viewers/", ViewerListView.as_view(), name="viewers"),
]

# API routes (grouped and isolated in the 'api' namespace)
urlpatterns += [
    path("api/", include((router.urls, "api"), namespace="api")),
    # API endpoints for user-specific watchlist and seen films
    path("api/user/watchlist/", user_watchlist, name="user_watchlist"),
    path("api/user/seen_films/", user_seen_films, name="user_seen_films"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
