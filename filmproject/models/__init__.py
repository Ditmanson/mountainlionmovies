# filmproject/models/__init__.py
from .film_informational_models import Collection, Company, Country, Film, Genre, Keyword, Language, Person
from .linking_tables import (
    LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, 
    LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages,
    LT_Viewer_Cosine_Similarity, LT_Viewer_Ratings, LT_Viewer_Seen, LT_Viewer_Watchlist
)
from .social_models import Viewer, FriendRequest, FeedEntry, Like, Comment, Notification, User
from .instant_messaging_models import *