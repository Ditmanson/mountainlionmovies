
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


from datetime import date
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class LT_Films_Cast(models.Model):
    film = models.ForeignKey(
        "filmproject.Film", on_delete=models.DO_NOTHING, null=True
    )
    person = models.ForeignKey(
        "filmproject.Person", on_delete=models.DO_NOTHING, null=True
    )
    cast_id = models.IntegerField()
    character = models.CharField(null=True, max_length=200)
    credit_id = models.CharField(max_length=200, null=True)
    order = models.IntegerField(null=True)


class LT_Films_Companies(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    company = models.ForeignKey(
        "filmproject.Company", on_delete=models.DO_NOTHING
    )


class LT_Films_Countries(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    country = models.ForeignKey(
        "filmproject.Country", on_delete=models.DO_NOTHING
    )


class LT_Films_Crew(models.Model):
    film = models.ForeignKey(
        "filmproject.Film", on_delete=models.DO_NOTHING, null=True
    )
    person = models.ForeignKey(
        "filmproject.Person", on_delete=models.DO_NOTHING, null=True
    )
    credit_id = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)
    job = models.CharField(max_length=200, null=True)


class LT_Films_Genres(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    genre = models.ForeignKey("filmproject.Genre", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("film", "genre")


class LT_Films_Keywords(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    keyword = models.ForeignKey(
        "filmproject.Keyword", on_delete=models.DO_NOTHING
    )

    def xǁLT_Films_Keywordsǁget_absolute_url__mutmut_orig(self):
        return reverse("LT_Films_Keywords-detail", args=[str(self.id)])

    def xǁLT_Films_Keywordsǁget_absolute_url__mutmut_1(self):
        return reverse("XXLT_Films_Keywords-detailXX", args=[str(self.id)])

    def xǁLT_Films_Keywordsǁget_absolute_url__mutmut_2(self):
        return reverse("LT_Films_Keywords-detail",)

    xǁLT_Films_Keywordsǁget_absolute_url__mutmut_mutants = {
    'xǁLT_Films_Keywordsǁget_absolute_url__mutmut_1': xǁLT_Films_Keywordsǁget_absolute_url__mutmut_1, 
        'xǁLT_Films_Keywordsǁget_absolute_url__mutmut_2': xǁLT_Films_Keywordsǁget_absolute_url__mutmut_2
    }

    def get_absolute_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLT_Films_Keywordsǁget_absolute_url__mutmut_orig"), object.__getattribute__(self, "xǁLT_Films_Keywordsǁget_absolute_url__mutmut_mutants"), *args, **kwargs)
        return result 

    get_absolute_url.__signature__ = _mutmut_signature(xǁLT_Films_Keywordsǁget_absolute_url__mutmut_orig)
    xǁLT_Films_Keywordsǁget_absolute_url__mutmut_orig.__name__ = 'xǁLT_Films_Keywordsǁget_absolute_url'



    class Meta:
        unique_together = ("film", "keyword")


class LT_Films_Languages(models.Model):
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    language = models.ForeignKey(
        "filmproject.Language", on_delete=models.DO_NOTHING
    )


class LT_Viewer_Cosine_Similarity(models.Model):
    viewer_1 = models.ForeignKey(
        "filmproject.Viewer", on_delete=models.PROTECT, related_name="viewer_1"
    )
    viewer_2 = models.ForeignKey(
        "filmproject.Viewer", on_delete=models.PROTECT, related_name="viewer_2"
    )
    cosine_similarity = models.DecimalField(
        decimal_places=4, max_digits=5, null=True
    )

    class Meta:
        unique_together = ("viewer_1", "viewer_2")
        indexes = [
            models.Index(fields=["viewer_1", "viewer_2"]),
        ]

    def xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_orig(self):
        if self.viewer_1 == self.viewer_2:
            raise ValidationError(
                "A viewer cannot have a cosine similarity score with themselves."
            )

    def xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_1(self):
        if self.viewer_1 != self.viewer_2:
            raise ValidationError(
                "A viewer cannot have a cosine similarity score with themselves."
            )

    def xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_2(self):
        if self.viewer_1 == self.viewer_2:
            raise ValidationError(
                "XXA viewer cannot have a cosine similarity score with themselves.XX"
            )

    xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_mutants = {
    'xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_1': xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_1, 
        'xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_2': xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_2
    }

    def clean(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_orig"), object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_mutants"), *args, **kwargs)
        return result 

    clean.__signature__ = _mutmut_signature(xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_orig)
    xǁLT_Viewer_Cosine_Similarityǁclean__mutmut_orig.__name__ = 'xǁLT_Viewer_Cosine_Similarityǁclean'



    def xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_orig(self, *args, **kwargs):
        if self.viewer_1.id > self.viewer_2.id:
            self.viewer_1, self.viewer_2 = self.viewer_2, self.viewer_1
        super().save(*args, **kwargs)

    def xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_1(self, *args, **kwargs):
        if self.viewer_1.id >= self.viewer_2.id:
            self.viewer_1, self.viewer_2 = self.viewer_2, self.viewer_1
        super().save(*args, **kwargs)

    def xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_2(self, *args, **kwargs):
        if self.viewer_1.id > self.viewer_2.id:
            self.viewer_1, self.viewer_2 = None
        super().save(*args, **kwargs)

    def xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_3(self, *args, **kwargs):
        if self.viewer_1.id > self.viewer_2.id:
            self.viewer_1, self.viewer_2 = self.viewer_2, self.viewer_1
        super().save( **kwargs)

    def xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_4(self, *args, **kwargs):
        if self.viewer_1.id > self.viewer_2.id:
            self.viewer_1, self.viewer_2 = self.viewer_2, self.viewer_1
        super().save(*args,)

    xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_mutants = {
    'xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_1': xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_1, 
        'xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_2': xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_2, 
        'xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_3': xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_3, 
        'xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_4': xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_4
    }

    def save(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_orig"), object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_mutants"), *args, **kwargs)
        return result 

    save.__signature__ = _mutmut_signature(xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_orig)
    xǁLT_Viewer_Cosine_Similarityǁsave__mutmut_orig.__name__ = 'xǁLT_Viewer_Cosine_Similarityǁsave'



    def xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_orig(self):
        return f"Cosine Similarity between {self.viewer_1} and {self.viewer_2}: {self.cosine_similarity}"

    xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_mutants = {

    }

    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_mutants"), *args, **kwargs)
        return result 

    __str__.__signature__ = _mutmut_signature(xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_orig)
    xǁLT_Viewer_Cosine_Similarityǁ__str____mutmut_orig.__name__ = 'xǁLT_Viewer_Cosine_Similarityǁ__str__'




class LT_Viewer_Ratings(models.Model):
    viewer = models.ForeignKey(
        "filmproject.Viewer", on_delete=models.DO_NOTHING, null=True
    )
    film_a = models.ForeignKey(
        "filmproject.Film",
        on_delete=models.DO_NOTHING,
        related_name="film_a",
        null=True,
    )
    film_b = models.ForeignKey(
        "filmproject.Film",
        on_delete=models.DO_NOTHING,
        related_name="film_b",
        null=True,
    )
    date = models.DateField(default=date.today, null=True)
    a_points = models.DecimalField(
        decimal_places=1, max_digits=3, default=0, null=True
    )
    b_points = models.DecimalField(
        decimal_places=1, max_digits=3, default=0, null=True
    )

    class Meta:
        unique_together = ("viewer", "film_a", "film_b")


class LT_Viewer_Seen(models.Model):
    viewer = models.ForeignKey(
        "filmproject.Viewer", on_delete=models.DO_NOTHING, null=True
    )
    film = models.ForeignKey(
        "filmproject.Film", on_delete=models.DO_NOTHING, null=True
    )
    seen_film = models.BooleanField(default=False, null=True)
    viewer_rating = models.DecimalField(
        decimal_places=8, max_digits=9, default=0.5, null=True
    )

    class Meta:
        unique_together = ("viewer", "film")


class LT_Viewer_Watchlist(models.Model):
    viewer = models.ForeignKey(
        "filmproject.Viewer", on_delete=models.DO_NOTHING
    )
    film = models.ForeignKey("filmproject.Film", on_delete=models.DO_NOTHING)
    watchlist = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["viewer", "film"]),
        ]
