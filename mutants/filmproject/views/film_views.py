
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


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from ..models import Film, LT_Viewer_Seen, LT_Viewer_Watchlist, Viewer


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "filmproject/film_detail.html"

    def xǁFilmDetailViewǁget_context_data__mutmut_orig(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_1(self, **kwargs):
        context = None
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_2(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = None

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_3(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = None
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_4(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["XXis_seenXX"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_5(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context[None] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_6(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(None)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_7(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = None
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_8(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["XXis_in_watchlistXX"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_9(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context[None] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_10(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(None)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_11(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = None
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_12(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["XXis_seenXX"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_13(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context[None] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_14(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = True
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_15(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = None
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_16(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["XXis_in_watchlistXX"] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_17(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context[None] = False

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_18(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = True

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_19(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = None

        context["film"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_20(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["XXfilmXX"] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_21(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context[None] = film
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_22(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = None
        context["mlm_rating"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_23(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["XXmlm_ratingXX"] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_24(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context[None] = film.mlm_rating
        return context

    def xǁFilmDetailViewǁget_context_data__mutmut_25(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()

        # Ensure Viewer object exists
        if self.request.user.is_authenticated:
            viewer, _ = Viewer.objects.get_or_create(user=self.request.user)
            context["is_seen"] = viewer.has_seen_film(film)
            context["is_in_watchlist"] = viewer.is_in_watchlist(film)
        else:
            context["is_seen"] = False
            context["is_in_watchlist"] = False

        context["film"] = film
        context["mlm_rating"] = None
        return context

    xǁFilmDetailViewǁget_context_data__mutmut_mutants = {
    'xǁFilmDetailViewǁget_context_data__mutmut_1': xǁFilmDetailViewǁget_context_data__mutmut_1, 
        'xǁFilmDetailViewǁget_context_data__mutmut_2': xǁFilmDetailViewǁget_context_data__mutmut_2, 
        'xǁFilmDetailViewǁget_context_data__mutmut_3': xǁFilmDetailViewǁget_context_data__mutmut_3, 
        'xǁFilmDetailViewǁget_context_data__mutmut_4': xǁFilmDetailViewǁget_context_data__mutmut_4, 
        'xǁFilmDetailViewǁget_context_data__mutmut_5': xǁFilmDetailViewǁget_context_data__mutmut_5, 
        'xǁFilmDetailViewǁget_context_data__mutmut_6': xǁFilmDetailViewǁget_context_data__mutmut_6, 
        'xǁFilmDetailViewǁget_context_data__mutmut_7': xǁFilmDetailViewǁget_context_data__mutmut_7, 
        'xǁFilmDetailViewǁget_context_data__mutmut_8': xǁFilmDetailViewǁget_context_data__mutmut_8, 
        'xǁFilmDetailViewǁget_context_data__mutmut_9': xǁFilmDetailViewǁget_context_data__mutmut_9, 
        'xǁFilmDetailViewǁget_context_data__mutmut_10': xǁFilmDetailViewǁget_context_data__mutmut_10, 
        'xǁFilmDetailViewǁget_context_data__mutmut_11': xǁFilmDetailViewǁget_context_data__mutmut_11, 
        'xǁFilmDetailViewǁget_context_data__mutmut_12': xǁFilmDetailViewǁget_context_data__mutmut_12, 
        'xǁFilmDetailViewǁget_context_data__mutmut_13': xǁFilmDetailViewǁget_context_data__mutmut_13, 
        'xǁFilmDetailViewǁget_context_data__mutmut_14': xǁFilmDetailViewǁget_context_data__mutmut_14, 
        'xǁFilmDetailViewǁget_context_data__mutmut_15': xǁFilmDetailViewǁget_context_data__mutmut_15, 
        'xǁFilmDetailViewǁget_context_data__mutmut_16': xǁFilmDetailViewǁget_context_data__mutmut_16, 
        'xǁFilmDetailViewǁget_context_data__mutmut_17': xǁFilmDetailViewǁget_context_data__mutmut_17, 
        'xǁFilmDetailViewǁget_context_data__mutmut_18': xǁFilmDetailViewǁget_context_data__mutmut_18, 
        'xǁFilmDetailViewǁget_context_data__mutmut_19': xǁFilmDetailViewǁget_context_data__mutmut_19, 
        'xǁFilmDetailViewǁget_context_data__mutmut_20': xǁFilmDetailViewǁget_context_data__mutmut_20, 
        'xǁFilmDetailViewǁget_context_data__mutmut_21': xǁFilmDetailViewǁget_context_data__mutmut_21, 
        'xǁFilmDetailViewǁget_context_data__mutmut_22': xǁFilmDetailViewǁget_context_data__mutmut_22, 
        'xǁFilmDetailViewǁget_context_data__mutmut_23': xǁFilmDetailViewǁget_context_data__mutmut_23, 
        'xǁFilmDetailViewǁget_context_data__mutmut_24': xǁFilmDetailViewǁget_context_data__mutmut_24, 
        'xǁFilmDetailViewǁget_context_data__mutmut_25': xǁFilmDetailViewǁget_context_data__mutmut_25
    }

    def get_context_data(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmDetailViewǁget_context_data__mutmut_orig"), object.__getattribute__(self, "xǁFilmDetailViewǁget_context_data__mutmut_mutants"), *args, **kwargs)
        return result 

    get_context_data.__signature__ = _mutmut_signature(xǁFilmDetailViewǁget_context_data__mutmut_orig)
    xǁFilmDetailViewǁget_context_data__mutmut_orig.__name__ = 'xǁFilmDetailViewǁget_context_data'



    def xǁFilmDetailViewǁpost__mutmut_orig(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_1(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_2(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('XXloginXX')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_3(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = None
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_4(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = None
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_5(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("XXactionXX")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_6(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = None
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_7(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("XXratingXX")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_8(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = None

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_9(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action != "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_10(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "XXmark_as_seenXX":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_11(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=None, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_12(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=None
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_13(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create( film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_14(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer,
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_15(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = None
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_16(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = False
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_17(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = None
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_18(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(None)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_19(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = None
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_20(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action != "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_21(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "XXremove_from_seenXX":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_22(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=None, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_23(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=None).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_24(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter( film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_25(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer,).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_26(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=True
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_27(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action != "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_28(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "XXadd_to_watchlistXX":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_29(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=None, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_30(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=None
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_31(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create( film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_32(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer,
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_33(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = None
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_34(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = False
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_35(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = None
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_36(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action != "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_37(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "XXremove_from_watchlistXX":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_38(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=None, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_39(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=None
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_40(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter( film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_41(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer,
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_42(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=True)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_43(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("XXfilm-detailXX", pk=film.id)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_44(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail",)

        return redirect("film-detail", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_45(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("XXfilm-detailXX", pk=film.id)

    def xǁFilmDetailViewǁpost__mutmut_46(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film = self.get_object()
        viewer, _ = Viewer.objects.get_or_create(user=request.user)
        action = request.POST.get("action")
        rating = request.POST.get("rating")

        try:
            if action == "mark_as_seen":
                seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                    viewer=viewer, film=film
                )
                seen_entry.seen_film = True
                if rating:
                    seen_entry.viewer_rating = float(rating)
                seen_entry.save()

            elif action == "remove_from_seen":
                LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                    seen_film=False
                )

            elif action == "add_to_watchlist":
                watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                    viewer=viewer, film=film
                )
                watchlist_entry.watchlist = True
                watchlist_entry.save()

            elif action == "remove_from_watchlist":
                LT_Viewer_Watchlist.objects.filter(
                    viewer=viewer, film=film
                ).update(watchlist=False)

        except ValueError:
            return redirect("film-detail", pk=film.id)

        return redirect("film-detail",)

    xǁFilmDetailViewǁpost__mutmut_mutants = {
    'xǁFilmDetailViewǁpost__mutmut_1': xǁFilmDetailViewǁpost__mutmut_1, 
        'xǁFilmDetailViewǁpost__mutmut_2': xǁFilmDetailViewǁpost__mutmut_2, 
        'xǁFilmDetailViewǁpost__mutmut_3': xǁFilmDetailViewǁpost__mutmut_3, 
        'xǁFilmDetailViewǁpost__mutmut_4': xǁFilmDetailViewǁpost__mutmut_4, 
        'xǁFilmDetailViewǁpost__mutmut_5': xǁFilmDetailViewǁpost__mutmut_5, 
        'xǁFilmDetailViewǁpost__mutmut_6': xǁFilmDetailViewǁpost__mutmut_6, 
        'xǁFilmDetailViewǁpost__mutmut_7': xǁFilmDetailViewǁpost__mutmut_7, 
        'xǁFilmDetailViewǁpost__mutmut_8': xǁFilmDetailViewǁpost__mutmut_8, 
        'xǁFilmDetailViewǁpost__mutmut_9': xǁFilmDetailViewǁpost__mutmut_9, 
        'xǁFilmDetailViewǁpost__mutmut_10': xǁFilmDetailViewǁpost__mutmut_10, 
        'xǁFilmDetailViewǁpost__mutmut_11': xǁFilmDetailViewǁpost__mutmut_11, 
        'xǁFilmDetailViewǁpost__mutmut_12': xǁFilmDetailViewǁpost__mutmut_12, 
        'xǁFilmDetailViewǁpost__mutmut_13': xǁFilmDetailViewǁpost__mutmut_13, 
        'xǁFilmDetailViewǁpost__mutmut_14': xǁFilmDetailViewǁpost__mutmut_14, 
        'xǁFilmDetailViewǁpost__mutmut_15': xǁFilmDetailViewǁpost__mutmut_15, 
        'xǁFilmDetailViewǁpost__mutmut_16': xǁFilmDetailViewǁpost__mutmut_16, 
        'xǁFilmDetailViewǁpost__mutmut_17': xǁFilmDetailViewǁpost__mutmut_17, 
        'xǁFilmDetailViewǁpost__mutmut_18': xǁFilmDetailViewǁpost__mutmut_18, 
        'xǁFilmDetailViewǁpost__mutmut_19': xǁFilmDetailViewǁpost__mutmut_19, 
        'xǁFilmDetailViewǁpost__mutmut_20': xǁFilmDetailViewǁpost__mutmut_20, 
        'xǁFilmDetailViewǁpost__mutmut_21': xǁFilmDetailViewǁpost__mutmut_21, 
        'xǁFilmDetailViewǁpost__mutmut_22': xǁFilmDetailViewǁpost__mutmut_22, 
        'xǁFilmDetailViewǁpost__mutmut_23': xǁFilmDetailViewǁpost__mutmut_23, 
        'xǁFilmDetailViewǁpost__mutmut_24': xǁFilmDetailViewǁpost__mutmut_24, 
        'xǁFilmDetailViewǁpost__mutmut_25': xǁFilmDetailViewǁpost__mutmut_25, 
        'xǁFilmDetailViewǁpost__mutmut_26': xǁFilmDetailViewǁpost__mutmut_26, 
        'xǁFilmDetailViewǁpost__mutmut_27': xǁFilmDetailViewǁpost__mutmut_27, 
        'xǁFilmDetailViewǁpost__mutmut_28': xǁFilmDetailViewǁpost__mutmut_28, 
        'xǁFilmDetailViewǁpost__mutmut_29': xǁFilmDetailViewǁpost__mutmut_29, 
        'xǁFilmDetailViewǁpost__mutmut_30': xǁFilmDetailViewǁpost__mutmut_30, 
        'xǁFilmDetailViewǁpost__mutmut_31': xǁFilmDetailViewǁpost__mutmut_31, 
        'xǁFilmDetailViewǁpost__mutmut_32': xǁFilmDetailViewǁpost__mutmut_32, 
        'xǁFilmDetailViewǁpost__mutmut_33': xǁFilmDetailViewǁpost__mutmut_33, 
        'xǁFilmDetailViewǁpost__mutmut_34': xǁFilmDetailViewǁpost__mutmut_34, 
        'xǁFilmDetailViewǁpost__mutmut_35': xǁFilmDetailViewǁpost__mutmut_35, 
        'xǁFilmDetailViewǁpost__mutmut_36': xǁFilmDetailViewǁpost__mutmut_36, 
        'xǁFilmDetailViewǁpost__mutmut_37': xǁFilmDetailViewǁpost__mutmut_37, 
        'xǁFilmDetailViewǁpost__mutmut_38': xǁFilmDetailViewǁpost__mutmut_38, 
        'xǁFilmDetailViewǁpost__mutmut_39': xǁFilmDetailViewǁpost__mutmut_39, 
        'xǁFilmDetailViewǁpost__mutmut_40': xǁFilmDetailViewǁpost__mutmut_40, 
        'xǁFilmDetailViewǁpost__mutmut_41': xǁFilmDetailViewǁpost__mutmut_41, 
        'xǁFilmDetailViewǁpost__mutmut_42': xǁFilmDetailViewǁpost__mutmut_42, 
        'xǁFilmDetailViewǁpost__mutmut_43': xǁFilmDetailViewǁpost__mutmut_43, 
        'xǁFilmDetailViewǁpost__mutmut_44': xǁFilmDetailViewǁpost__mutmut_44, 
        'xǁFilmDetailViewǁpost__mutmut_45': xǁFilmDetailViewǁpost__mutmut_45, 
        'xǁFilmDetailViewǁpost__mutmut_46': xǁFilmDetailViewǁpost__mutmut_46
    }

    def post(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmDetailViewǁpost__mutmut_orig"), object.__getattribute__(self, "xǁFilmDetailViewǁpost__mutmut_mutants"), *args, **kwargs)
        return result 

    post.__signature__ = _mutmut_signature(xǁFilmDetailViewǁpost__mutmut_orig)
    xǁFilmDetailViewǁpost__mutmut_orig.__name__ = 'xǁFilmDetailViewǁpost'




class FilmListView(ListView):
    model = Film
    template_name = "film_list.html"
    context_object_name = "film_list"
    paginate_by = 20

    def xǁFilmListViewǁget_queryset__mutmut_orig(self):
        return Film.objects.all().order_by("-mlm_rating")

    def xǁFilmListViewǁget_queryset__mutmut_1(self):
        return Film.objects.all().order_by("XX-mlm_ratingXX")

    xǁFilmListViewǁget_queryset__mutmut_mutants = {
    'xǁFilmListViewǁget_queryset__mutmut_1': xǁFilmListViewǁget_queryset__mutmut_1
    }

    def get_queryset(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmListViewǁget_queryset__mutmut_orig"), object.__getattribute__(self, "xǁFilmListViewǁget_queryset__mutmut_mutants"), *args, **kwargs)
        return result 

    get_queryset.__signature__ = _mutmut_signature(xǁFilmListViewǁget_queryset__mutmut_orig)
    xǁFilmListViewǁget_queryset__mutmut_orig.__name__ = 'xǁFilmListViewǁget_queryset'



    def xǁFilmListViewǁpost__mutmut_orig(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_1(self, request, *args, **kwargs):
        if  request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_2(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('XXloginXX')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_3(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("XXfilm_idXX")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_4(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = None
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_5(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("XXactionXX")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_6(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = None
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_7(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("XXpageXX", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_8(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 2)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_9(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = None
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_10(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=None)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_11(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = None
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_12(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = None

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_13(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action != "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_14(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "XXmark_as_seenXX":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_15(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=None, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_16(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=None
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_17(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create( film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_18(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer,
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_19(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = None
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_20(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = False
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_21(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = None
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_22(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action != "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_23(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "XXremove_from_seenXX":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_24(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=None, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_25(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=None).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_26(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter( film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_27(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer,).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_28(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=True
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_29(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action != "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_30(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "XXadd_to_watchlistXX":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_31(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=None, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_32(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=None
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_33(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create( film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_34(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer,
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_35(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = None
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_36(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = False
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_37(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = None
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_38(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action != "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_39(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "XXremove_from_watchlistXX":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_40(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=None, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_41(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=None
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_42(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter( film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_43(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer,
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_44(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=True)

        return redirect(f"{reverse_lazy('film_list')}?page={page_number}")

    def xǁFilmListViewǁpost__mutmut_45(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse_lazy('login')}?next={request.path}")

        film_id = request.POST.get("film_id")
        action = request.POST.get("action")
        page_number = request.POST.get("page", 1)
        film = Film.objects.get(id=film_id)
        viewer = request.user.viewer

        if action == "mark_as_seen":
            seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
                viewer=viewer, film=film
            )
            seen_entry.seen_film = True
            seen_entry.save()
        elif action == "remove_from_seen":
            LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
                seen_film=False
            )
        elif action == "add_to_watchlist":
            watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
                viewer=viewer, film=film
            )
            watchlist_entry.watchlist = True
            watchlist_entry.save()
        elif action == "remove_from_watchlist":
            LT_Viewer_Watchlist.objects.filter(
                viewer=viewer, film=film
            ).update(watchlist=False)

        return redirect(f"{reverse_lazy('XXfilm_listXX')}?page={page_number}")

    xǁFilmListViewǁpost__mutmut_mutants = {
    'xǁFilmListViewǁpost__mutmut_1': xǁFilmListViewǁpost__mutmut_1, 
        'xǁFilmListViewǁpost__mutmut_2': xǁFilmListViewǁpost__mutmut_2, 
        'xǁFilmListViewǁpost__mutmut_3': xǁFilmListViewǁpost__mutmut_3, 
        'xǁFilmListViewǁpost__mutmut_4': xǁFilmListViewǁpost__mutmut_4, 
        'xǁFilmListViewǁpost__mutmut_5': xǁFilmListViewǁpost__mutmut_5, 
        'xǁFilmListViewǁpost__mutmut_6': xǁFilmListViewǁpost__mutmut_6, 
        'xǁFilmListViewǁpost__mutmut_7': xǁFilmListViewǁpost__mutmut_7, 
        'xǁFilmListViewǁpost__mutmut_8': xǁFilmListViewǁpost__mutmut_8, 
        'xǁFilmListViewǁpost__mutmut_9': xǁFilmListViewǁpost__mutmut_9, 
        'xǁFilmListViewǁpost__mutmut_10': xǁFilmListViewǁpost__mutmut_10, 
        'xǁFilmListViewǁpost__mutmut_11': xǁFilmListViewǁpost__mutmut_11, 
        'xǁFilmListViewǁpost__mutmut_12': xǁFilmListViewǁpost__mutmut_12, 
        'xǁFilmListViewǁpost__mutmut_13': xǁFilmListViewǁpost__mutmut_13, 
        'xǁFilmListViewǁpost__mutmut_14': xǁFilmListViewǁpost__mutmut_14, 
        'xǁFilmListViewǁpost__mutmut_15': xǁFilmListViewǁpost__mutmut_15, 
        'xǁFilmListViewǁpost__mutmut_16': xǁFilmListViewǁpost__mutmut_16, 
        'xǁFilmListViewǁpost__mutmut_17': xǁFilmListViewǁpost__mutmut_17, 
        'xǁFilmListViewǁpost__mutmut_18': xǁFilmListViewǁpost__mutmut_18, 
        'xǁFilmListViewǁpost__mutmut_19': xǁFilmListViewǁpost__mutmut_19, 
        'xǁFilmListViewǁpost__mutmut_20': xǁFilmListViewǁpost__mutmut_20, 
        'xǁFilmListViewǁpost__mutmut_21': xǁFilmListViewǁpost__mutmut_21, 
        'xǁFilmListViewǁpost__mutmut_22': xǁFilmListViewǁpost__mutmut_22, 
        'xǁFilmListViewǁpost__mutmut_23': xǁFilmListViewǁpost__mutmut_23, 
        'xǁFilmListViewǁpost__mutmut_24': xǁFilmListViewǁpost__mutmut_24, 
        'xǁFilmListViewǁpost__mutmut_25': xǁFilmListViewǁpost__mutmut_25, 
        'xǁFilmListViewǁpost__mutmut_26': xǁFilmListViewǁpost__mutmut_26, 
        'xǁFilmListViewǁpost__mutmut_27': xǁFilmListViewǁpost__mutmut_27, 
        'xǁFilmListViewǁpost__mutmut_28': xǁFilmListViewǁpost__mutmut_28, 
        'xǁFilmListViewǁpost__mutmut_29': xǁFilmListViewǁpost__mutmut_29, 
        'xǁFilmListViewǁpost__mutmut_30': xǁFilmListViewǁpost__mutmut_30, 
        'xǁFilmListViewǁpost__mutmut_31': xǁFilmListViewǁpost__mutmut_31, 
        'xǁFilmListViewǁpost__mutmut_32': xǁFilmListViewǁpost__mutmut_32, 
        'xǁFilmListViewǁpost__mutmut_33': xǁFilmListViewǁpost__mutmut_33, 
        'xǁFilmListViewǁpost__mutmut_34': xǁFilmListViewǁpost__mutmut_34, 
        'xǁFilmListViewǁpost__mutmut_35': xǁFilmListViewǁpost__mutmut_35, 
        'xǁFilmListViewǁpost__mutmut_36': xǁFilmListViewǁpost__mutmut_36, 
        'xǁFilmListViewǁpost__mutmut_37': xǁFilmListViewǁpost__mutmut_37, 
        'xǁFilmListViewǁpost__mutmut_38': xǁFilmListViewǁpost__mutmut_38, 
        'xǁFilmListViewǁpost__mutmut_39': xǁFilmListViewǁpost__mutmut_39, 
        'xǁFilmListViewǁpost__mutmut_40': xǁFilmListViewǁpost__mutmut_40, 
        'xǁFilmListViewǁpost__mutmut_41': xǁFilmListViewǁpost__mutmut_41, 
        'xǁFilmListViewǁpost__mutmut_42': xǁFilmListViewǁpost__mutmut_42, 
        'xǁFilmListViewǁpost__mutmut_43': xǁFilmListViewǁpost__mutmut_43, 
        'xǁFilmListViewǁpost__mutmut_44': xǁFilmListViewǁpost__mutmut_44, 
        'xǁFilmListViewǁpost__mutmut_45': xǁFilmListViewǁpost__mutmut_45
    }

    def post(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmListViewǁpost__mutmut_orig"), object.__getattribute__(self, "xǁFilmListViewǁpost__mutmut_mutants"), *args, **kwargs)
        return result 

    post.__signature__ = _mutmut_signature(xǁFilmListViewǁpost__mutmut_orig)
    xǁFilmListViewǁpost__mutmut_orig.__name__ = 'xǁFilmListViewǁpost'



    def xǁFilmListViewǁget_context_data__mutmut_orig(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_1(self, **kwargs):
        context = None
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_2(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = None
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_3(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["XXseen_filmsXX"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_4(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context[None] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_5(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=None, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_6(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=False
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_7(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter( lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_8(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer,
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_9(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = None
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_10(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["XXwatchlist_filmsXX"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_11(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context[None] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_12(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=None,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_13(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=False,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_14(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_15(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_16(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = None
        else:
            context["seen_films"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_17(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["XXseen_filmsXX"] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_18(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context[None] = []
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_19(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = None
            context["watchlist_films"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_20(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["XXwatchlist_filmsXX"] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_21(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context[None] = []
        return context

    def xǁFilmListViewǁget_context_data__mutmut_22(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            viewer = self.request.user.viewer
            context["seen_films"] = Film.objects.filter(
                lt_viewer_seen__viewer=viewer, lt_viewer_seen__seen_film=True
            )
            context["watchlist_films"] = Film.objects.filter(
                lt_viewer_watchlist__viewer=viewer,
                lt_viewer_watchlist__watchlist=True,
            )
        else:
            context["seen_films"] = []
            context["watchlist_films"] = None
        return context

    xǁFilmListViewǁget_context_data__mutmut_mutants = {
    'xǁFilmListViewǁget_context_data__mutmut_1': xǁFilmListViewǁget_context_data__mutmut_1, 
        'xǁFilmListViewǁget_context_data__mutmut_2': xǁFilmListViewǁget_context_data__mutmut_2, 
        'xǁFilmListViewǁget_context_data__mutmut_3': xǁFilmListViewǁget_context_data__mutmut_3, 
        'xǁFilmListViewǁget_context_data__mutmut_4': xǁFilmListViewǁget_context_data__mutmut_4, 
        'xǁFilmListViewǁget_context_data__mutmut_5': xǁFilmListViewǁget_context_data__mutmut_5, 
        'xǁFilmListViewǁget_context_data__mutmut_6': xǁFilmListViewǁget_context_data__mutmut_6, 
        'xǁFilmListViewǁget_context_data__mutmut_7': xǁFilmListViewǁget_context_data__mutmut_7, 
        'xǁFilmListViewǁget_context_data__mutmut_8': xǁFilmListViewǁget_context_data__mutmut_8, 
        'xǁFilmListViewǁget_context_data__mutmut_9': xǁFilmListViewǁget_context_data__mutmut_9, 
        'xǁFilmListViewǁget_context_data__mutmut_10': xǁFilmListViewǁget_context_data__mutmut_10, 
        'xǁFilmListViewǁget_context_data__mutmut_11': xǁFilmListViewǁget_context_data__mutmut_11, 
        'xǁFilmListViewǁget_context_data__mutmut_12': xǁFilmListViewǁget_context_data__mutmut_12, 
        'xǁFilmListViewǁget_context_data__mutmut_13': xǁFilmListViewǁget_context_data__mutmut_13, 
        'xǁFilmListViewǁget_context_data__mutmut_14': xǁFilmListViewǁget_context_data__mutmut_14, 
        'xǁFilmListViewǁget_context_data__mutmut_15': xǁFilmListViewǁget_context_data__mutmut_15, 
        'xǁFilmListViewǁget_context_data__mutmut_16': xǁFilmListViewǁget_context_data__mutmut_16, 
        'xǁFilmListViewǁget_context_data__mutmut_17': xǁFilmListViewǁget_context_data__mutmut_17, 
        'xǁFilmListViewǁget_context_data__mutmut_18': xǁFilmListViewǁget_context_data__mutmut_18, 
        'xǁFilmListViewǁget_context_data__mutmut_19': xǁFilmListViewǁget_context_data__mutmut_19, 
        'xǁFilmListViewǁget_context_data__mutmut_20': xǁFilmListViewǁget_context_data__mutmut_20, 
        'xǁFilmListViewǁget_context_data__mutmut_21': xǁFilmListViewǁget_context_data__mutmut_21, 
        'xǁFilmListViewǁget_context_data__mutmut_22': xǁFilmListViewǁget_context_data__mutmut_22
    }

    def get_context_data(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFilmListViewǁget_context_data__mutmut_orig"), object.__getattribute__(self, "xǁFilmListViewǁget_context_data__mutmut_mutants"), *args, **kwargs)
        return result 

    get_context_data.__signature__ = _mutmut_signature(xǁFilmListViewǁget_context_data__mutmut_orig)
    xǁFilmListViewǁget_context_data__mutmut_orig.__name__ = 'xǁFilmListViewǁget_context_data'




@login_required
def add_to_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        watchlist_entry, _ = LT_Viewer_Watchlist.objects.get_or_create(
            viewer=viewer, film=film
        )
        watchlist_entry.watchlist = True
        watchlist_entry.save()
    return redirect("film-detail", pk=pk)


def x_index__mutmut_orig(request):
    return render(request, "filmproject/index.html")


def x_index__mutmut_1(request):
    return render(None, "filmproject/index.html")


def x_index__mutmut_2(request):
    return render(request, "XXfilmproject/index.htmlXX")


def x_index__mutmut_3(request):
    return render( "filmproject/index.html")

x_index__mutmut_mutants = {
'x_index__mutmut_1': x_index__mutmut_1, 
    'x_index__mutmut_2': x_index__mutmut_2, 
    'x_index__mutmut_3': x_index__mutmut_3
}

def index(*args, **kwargs):
    result = _mutmut_trampoline(x_index__mutmut_orig, x_index__mutmut_mutants, *args, **kwargs)
    return result 

index.__signature__ = _mutmut_signature(x_index__mutmut_orig)
x_index__mutmut_orig.__name__ = 'x_index'




@login_required
def mark_as_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer

    if request.method == "POST":
        seen_entry, _ = LT_Viewer_Seen.objects.get_or_create(
            viewer=viewer, film=film
        )
        seen_entry.seen_film = True
        seen_entry.viewer_rating = seen_entry.viewer_rating or 0.5
        seen_entry.save()

    return redirect("film-detail", pk=pk)


@login_required
def remove_from_seen(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Seen.objects.filter(viewer=viewer, film=film).update(
            seen_film=False
        )
    return redirect("film-detail", pk=pk)


@login_required
def remove_from_watchlist(request, pk):
    film = get_object_or_404(Film, id=pk)
    viewer = request.user.viewer
    if request.method == "POST":
        LT_Viewer_Watchlist.objects.filter(viewer=viewer, film=film).update(
            watchlist=False
        )
    return redirect("film-detail", pk=pk)


def x_search_movies__mutmut_orig(request):
    return render(request, "filmproject/search_movies.html")


def x_search_movies__mutmut_1(request):
    return render(None, "filmproject/search_movies.html")


def x_search_movies__mutmut_2(request):
    return render(request, "XXfilmproject/search_movies.htmlXX")


def x_search_movies__mutmut_3(request):
    return render( "filmproject/search_movies.html")

x_search_movies__mutmut_mutants = {
'x_search_movies__mutmut_1': x_search_movies__mutmut_1, 
    'x_search_movies__mutmut_2': x_search_movies__mutmut_2, 
    'x_search_movies__mutmut_3': x_search_movies__mutmut_3
}

def search_movies(*args, **kwargs):
    result = _mutmut_trampoline(x_search_movies__mutmut_orig, x_search_movies__mutmut_mutants, *args, **kwargs)
    return result 

search_movies.__signature__ = _mutmut_signature(x_search_movies__mutmut_orig)
x_search_movies__mutmut_orig.__name__ = 'x_search_movies'


