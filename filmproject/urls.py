from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

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
# router.register(r"notifications", NotificationsViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accept_friend_request/<int:request_id>/", accept_friend_request, name="accept_friend_request"),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("activation/invalid/", render_invalid_activation_page, name="invalid_activation"),
    path("api/", include((router.urls, "api"), namespace="api")),
    path("api/user/seen_films/", user_seen_films, name="user_seen_films"),
    path("api/user/watchlist/", user_watchlist, name="user_watchlist"),
    # path("comment_entry/<int:entry_id>/", comment_entry, name="comment_entry"),
    path("compare_movies/", compare_movies, name="compare_movies"),
    path("compare_movies/submit_selection/", submit_movie_selection, name="submit_movie_selection"),
    path("feed/", feed_page, name="feed_page"),
    path("feed_entries/", feed_entries, name="feed_entries"),
    path("feed_entry/<int:entry_id>/", feed_entry_detail, name="feed_entry_detail"),
    path("films/", FilmListView.as_view(), name="film_list"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film-detail"),
    path("films/<int:pk>/add_to_watchlist/", add_to_watchlist, name="add_to_watchlist"),
    path("films/<int:pk>/mark_as_seen/", mark_as_seen, name="mark_as_seen"),
    path("films/<int:pk>/remove_from_seen/", remove_from_seen, name="remove_from_seen"),
    path("films/<int:pk>/remove_from_watchlist/", remove_from_watchlist, name="remove_from_watchlist"),
    path("index", IndexView.as_view(), name="index"), # Is this one redundant? (Bob)
    # path("like_entry/<int:entry_id>/", like_entry, name="like_entry"),
    path("login/", auth_views.LoginView.as_view(template_name="filmproject/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="filmproject/index.html"), name="logout"),
    path('new-movies/', views.load_new_movies, name='load_new_movies'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="filmproject/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="filmproject/password_reset_done.html"), name="password_reset_done"),
    path('popular-movies/', views.load_popular_movies, name='load_popular_movies'),
    path("profile/<int:viewer_id>/", ProfileView.as_view(), name="profile_viewer"),
    path('recommendations/', views.load_recommendations, name='load_recommendations'),
    path("register/", register, name="register"),
    path("reject_friend_request/<int:request_id>/", reject_friend_request, name="reject_friend_request"),
    path("remove_friend/<int:viewer_id>/", remove_friend, name="remove_friend"),
    path("resend-activation/<str:uidb64>/", resend_activation_email, name="resend_activation"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="filmproject/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="filmproject/password_reset_complete.html"), name="password_reset_complete"),
    path("search_movies/", search_movies, name="search_movies"),
    path("search_results/", search_results, name="search_results"),
    path("send_friend_request/<int:viewer_id>/", send_friend_request, name="send_friend_request"),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    path('super/calculate-cosine-similarity/', manual_calculate_cosine_similarity, name='manual_calculate_cosine_similarity'),
    path('super/database-cleanup/', manual_database_cleanup, name='manual_database_cleanup'),
    path('super/recalculate-recommendations/', manual_recalculate_recommendations, name='manual_recalculate_recommendations'),
    path('super/update-film-ratings/', manual_update_film_ratings, name='manual_update_film_ratings'),
    path("update_profile/<int:pk>/", update_profile, name="update_profile"),
    path("viewers/", ViewerListView.as_view(), name="viewers"),
    path('watchlist/', views.load_watchlist, name='load_watchlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
