
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


from django.core.management.base import BaseCommand
from filmproject.models import Film


class Command(BaseCommand):
    help = "Update MLM ratings for all films"

    def xǁCommandǁhandle__mutmut_orig(self, *args, **kwargs):
        films = Film.objects.all()
        for film in films:
            film.update_mlm_rating()
            self.stdout.write(f"Updated MLM rating for: {film.title}")

    def xǁCommandǁhandle__mutmut_1(self, *args, **kwargs):
        films = None
        for film in films:
            film.update_mlm_rating()
            self.stdout.write(f"Updated MLM rating for: {film.title}")

    xǁCommandǁhandle__mutmut_mutants = {
    'xǁCommandǁhandle__mutmut_1': xǁCommandǁhandle__mutmut_1
    }

    def handle(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCommandǁhandle__mutmut_orig"), object.__getattribute__(self, "xǁCommandǁhandle__mutmut_mutants"), *args, **kwargs)
        return result 

    handle.__signature__ = _mutmut_signature(xǁCommandǁhandle__mutmut_orig)
    xǁCommandǁhandle__mutmut_orig.__name__ = 'xǁCommandǁhandle'


