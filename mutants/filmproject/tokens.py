
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


from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_orig(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )
    def xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_1(self, user, timestamp):
        return (
            six.text_type(user.pk)
            - six.text_type(timestamp)
            + six.text_type(user.is_active)
        )
    def xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_2(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(None)
            + six.text_type(user.is_active)
        )
    def xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_3(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            - six.text_type(user.is_active)
        )

    xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_mutants = {
    'xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_1': xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_1, 
        'xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_2': xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_2, 
        'xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_3': xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_3
    }

    def _make_hash_value(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_orig"), object.__getattribute__(self, "xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_mutants"), *args, **kwargs)
        return result 

    _make_hash_value.__signature__ = _mutmut_signature(xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_orig)
    xǁAccountActivationTokenGeneratorǁ_make_hash_value__mutmut_orig.__name__ = 'xǁAccountActivationTokenGeneratorǁ_make_hash_value'




account_activation_token = AccountActivationTokenGenerator()
