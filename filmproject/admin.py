from django.contrib import admin
from .models import Collection, Company, Country, Film, Genre, Keyword, Language, Person, Viewer, LT_Films_Cast, LT_Films_Companies, LT_Films_Countries, LT_Films_Crew, LT_Films_Genres, LT_Films_Keywords, LT_Films_Languages, LT_Viewer_Ratings, LT_Viewer_Seen, LT_Viewer_Watchlist

admin.site.register(Collection)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Keyword)
admin.site.register(Language)
admin.site.register(Person)
admin.site.register(Viewer)
admin.site.register(LT_Films_Cast)
admin.site.register(LT_Films_Companies)
admin.site.register(LT_Films_Countries)
admin.site.register(LT_Films_Crew)
admin.site.register(LT_Films_Genres)
admin.site.register(LT_Films_Keywords)
admin.site.register(LT_Films_Languages)
admin.site.register(LT_Viewer_Ratings)
admin.site.register(LT_Viewer_Seen)
admin.site.register(LT_Viewer_Watchlist)