
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


from django.contrib import admin
from .models import (
    Collection,
    Company,
    Country,
    Film,
    Genre,
    Keyword,
    Language,
    Person,
    Viewer,
    LT_Films_Cast,
    LT_Films_Companies,
    LT_Films_Countries,
    LT_Films_Crew,
    LT_Films_Genres,
    LT_Films_Keywords,
    LT_Films_Languages,
    LT_Viewer_Cosine_Similarity,
    LT_Viewer_Ratings,
    LT_Viewer_Seen,
    LT_Viewer_Watchlist,
    FriendRequest,
    FeedEntry,
    Like,
    Comment,
)

# Register models
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
admin.site.register(LT_Viewer_Cosine_Similarity)
admin.site.register(LT_Viewer_Ratings)
admin.site.register(LT_Viewer_Seen)
admin.site.register(LT_Viewer_Watchlist)
admin.site.register(FriendRequest)
admin.site.register(FeedEntry)
admin.site.register(Like)
admin.site.register(Comment)
