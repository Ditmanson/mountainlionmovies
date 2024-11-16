
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


from django.db import models
from django.urls import reverse


class Collection(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)

    def xǁCollectionǁ__str____mutmut_orig(self):
        return self.name

    xǁCollectionǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCollectionǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCollectionǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCollectionǁ__str____mutmut_orig)
    xǁCollectionǁ__str____mutmut_orig.__name__ = 'xǁCollectionǁ__str__'




class Company(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    company = models.CharField(max_length=200)

    def xǁCompanyǁ__str____mutmut_orig(self):
        return self.company

    xǁCompanyǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCompanyǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCompanyǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCompanyǁ__str____mutmut_orig)
    xǁCompanyǁ__str____mutmut_orig.__name__ = 'xǁCompanyǁ__str__'




class Country(models.Model):
    code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)

    def xǁCountryǁ__str____mutmut_orig(self):
        return self.country

    xǁCountryǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCountryǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCountryǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁCountryǁ__str____mutmut_orig)
    xǁCountryǁ__str____mutmut_orig.__name__ = 'xǁCountryǁ__str__'




class Film(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    backdrop_path = models.CharField(max_length=200, blank=True, null=True)
    belongs_to_collection = models.BooleanField(default=False)
    budget = models.IntegerField(null=True)
    homepage = models.CharField(max_length=200, blank=True, null=True)
    imdb_id = models.CharField(max_length=20, blank=True, null=True)
    original_title = models.CharField(max_length=200)
    overview = models.CharField(max_length=2000, blank=True, null=True)
    popularity = models.DecimalField(decimal_places=6, max_digits=20)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    revenue = models.BigIntegerField(null=True)
    runtime = models.IntegerField(null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    tagline = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=200)
    tmdb_id = models.IntegerField(unique=True, null=True)
    vote_average = models.DecimalField(
        decimal_places=3, max_digits=6, null=True, blank=True
    )
    vote_count = models.IntegerField(null=True)
    mlm_rating = models.DecimalField(
        decimal_places=6, max_digits=20, null=True
    )

    def xǁFilmǁ__str____mutmut_orig(self):
        return self.title

    xǁFilmǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁFilmǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁFilmǁ__str____mutmut_orig)
    xǁFilmǁ__str____mutmut_orig.__name__ = 'xǁFilmǁ__str__'



    def xǁFilmǁget_absolute_url__mutmut_orig(self):
        return reverse("film-detail", args=[str(self.id)])

    def xǁFilmǁget_absolute_url__mutmut_1(self):
        return reverse("XXfilm-detailXX", args=[str(self.id)])

    def xǁFilmǁget_absolute_url__mutmut_2(self):
        return reverse("film-detail",)

    xǁFilmǁget_absolute_url__mutmut_mutants = {
    'xǁFilmǁget_absolute_url__mutmut_1': xǁFilmǁget_absolute_url__mutmut_1, 
        'xǁFilmǁget_absolute_url__mutmut_2': xǁFilmǁget_absolute_url__mutmut_2
    }

    def get_absolute_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmǁget_absolute_url__mutmut_orig"), object.__getattribute__(self, "xǁFilmǁget_absolute_url__mutmut_mutants"), *args, **kwargs)
        return result 

    get_absolute_url.__signature__ = _mutmut_signature(xǁFilmǁget_absolute_url__mutmut_orig)
    xǁFilmǁget_absolute_url__mutmut_orig.__name__ = 'xǁFilmǁget_absolute_url'




class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    genre = models.CharField(unique=True, max_length=200)

    def xǁGenreǁ__str____mutmut_orig(self):
        return self.genre

    xǁGenreǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁGenreǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁGenreǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁGenreǁ__str____mutmut_orig)
    xǁGenreǁ__str____mutmut_orig.__name__ = 'xǁGenreǁ__str__'




class Keyword(models.Model):
    tmdb_id = models.IntegerField(unique=True, null=True)
    keyword = models.CharField(unique=True, max_length=200)

    def xǁKeywordǁ__str____mutmut_orig(self):
        return self.keyword

    xǁKeywordǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁKeywordǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁKeywordǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁKeywordǁ__str____mutmut_orig)
    xǁKeywordǁ__str____mutmut_orig.__name__ = 'xǁKeywordǁ__str__'




class Language(models.Model):
    code = models.CharField(null=True, unique=True, max_length=4)
    language = models.CharField(null=True, max_length=200)

    def xǁLanguageǁ__str____mutmut_orig(self):
        return self.language

    xǁLanguageǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLanguageǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁLanguageǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁLanguageǁ__str____mutmut_orig)
    xǁLanguageǁ__str____mutmut_orig.__name__ = 'xǁLanguageǁ__str__'




class Person(models.Model):
    adult = models.BooleanField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    tmdb_id = models.IntegerField(unique=True)
    known_for_department = models.CharField(
        max_length=200, null=True, blank=True
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    popularity = models.DecimalField(
        decimal_places=3, null=True, blank=True, max_digits=10
    )
    profile_path = models.CharField(max_length=200, null=True, blank=True)

    def xǁPersonǁ__str____mutmut_orig(self):
        return self.name

    xǁPersonǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPersonǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁPersonǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁPersonǁ__str____mutmut_orig)
    xǁPersonǁ__str____mutmut_orig.__name__ = 'xǁPersonǁ__str__'



    def xǁPersonǁget_absolute_url__mutmut_orig(self):
        return reverse("person-detail", args=[str(self.id)])

    def xǁPersonǁget_absolute_url__mutmut_1(self):
        return reverse("XXperson-detailXX", args=[str(self.id)])

    def xǁPersonǁget_absolute_url__mutmut_2(self):
        return reverse("person-detail",)

    xǁPersonǁget_absolute_url__mutmut_mutants = {
    'xǁPersonǁget_absolute_url__mutmut_1': xǁPersonǁget_absolute_url__mutmut_1, 
        'xǁPersonǁget_absolute_url__mutmut_2': xǁPersonǁget_absolute_url__mutmut_2
    }

    def get_absolute_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPersonǁget_absolute_url__mutmut_orig"), object.__getattribute__(self, "xǁPersonǁget_absolute_url__mutmut_mutants"), *args, **kwargs)
        return result 

    get_absolute_url.__signature__ = _mutmut_signature(xǁPersonǁget_absolute_url__mutmut_orig)
    xǁPersonǁget_absolute_url__mutmut_orig.__name__ = 'xǁPersonǁget_absolute_url'


