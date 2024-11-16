
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


from django import template

register = template.Library()


@register.filter
def get_similarity(similarity_scores, viewer_id):
    score = similarity_scores.get(viewer_id, 0)  # Default to 0 if missing
    return f"{score * 100:.1f}%"  # Convert to percentage and format


def x_runtime_format__mutmut_orig(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_1(value):
    try:
        hours = value / 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_2(value):
    try:
        hours = value // 61
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_3(value):
    try:
        hours = None
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_4(value):
    try:
        hours = value // 60
        minutes = value / 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_5(value):
    try:
        hours = value // 60
        minutes = value % 61

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_6(value):
    try:
        hours = value // 60
        minutes = None

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_7(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours >= 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_8(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 2 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_9(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes >= 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_10(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 2:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_11(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 or minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_12(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours >= 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_13(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 2 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_14(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes != 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_15(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 2:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_16(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 or minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_17(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours >= 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_18(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 2 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_19(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes != 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_20(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_21(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 or minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_22(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours != 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_23(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 2 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_24(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes >= 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_25(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 2:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_26(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 or minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_27(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours != 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_28(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 2 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_29(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes != 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_30(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 2:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_31(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 or minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_32(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours != 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_33(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 2 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_34(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes != 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_35(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_36(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 or minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_37(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes >= 1:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_38(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 2:
            return f"{minutes} minutes"
        elif minutes == 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_39(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes != 1:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value


def x_runtime_format__mutmut_40(value):
    try:
        hours = value // 60
        minutes = value % 60

        if hours > 1 and minutes > 1:
            return f"{hours} hours, {minutes} minutes"
        elif hours > 1 and minutes == 1:
            return f"{hours} hours, {minutes} minute"
        elif hours > 1 and minutes == 0:
            return f"{hours} hours"
        elif hours == 1 and minutes > 1:
            return f"{hours} hour, {minutes} minutes"
        elif hours == 1 and minutes == 1:
            return f"{hours} hour, {minutes} minute"
        elif hours == 1 and minutes == 0:
            return f"{hours} hour"
        elif minutes > 1:
            return f"{minutes} minutes"
        elif minutes == 2:
            return f"{minutes} minute"
        else:
            return f"{minutes} minutes"
    except (ValueError, TypeError):
        return value

x_runtime_format__mutmut_mutants = {
'x_runtime_format__mutmut_1': x_runtime_format__mutmut_1, 
    'x_runtime_format__mutmut_2': x_runtime_format__mutmut_2, 
    'x_runtime_format__mutmut_3': x_runtime_format__mutmut_3, 
    'x_runtime_format__mutmut_4': x_runtime_format__mutmut_4, 
    'x_runtime_format__mutmut_5': x_runtime_format__mutmut_5, 
    'x_runtime_format__mutmut_6': x_runtime_format__mutmut_6, 
    'x_runtime_format__mutmut_7': x_runtime_format__mutmut_7, 
    'x_runtime_format__mutmut_8': x_runtime_format__mutmut_8, 
    'x_runtime_format__mutmut_9': x_runtime_format__mutmut_9, 
    'x_runtime_format__mutmut_10': x_runtime_format__mutmut_10, 
    'x_runtime_format__mutmut_11': x_runtime_format__mutmut_11, 
    'x_runtime_format__mutmut_12': x_runtime_format__mutmut_12, 
    'x_runtime_format__mutmut_13': x_runtime_format__mutmut_13, 
    'x_runtime_format__mutmut_14': x_runtime_format__mutmut_14, 
    'x_runtime_format__mutmut_15': x_runtime_format__mutmut_15, 
    'x_runtime_format__mutmut_16': x_runtime_format__mutmut_16, 
    'x_runtime_format__mutmut_17': x_runtime_format__mutmut_17, 
    'x_runtime_format__mutmut_18': x_runtime_format__mutmut_18, 
    'x_runtime_format__mutmut_19': x_runtime_format__mutmut_19, 
    'x_runtime_format__mutmut_20': x_runtime_format__mutmut_20, 
    'x_runtime_format__mutmut_21': x_runtime_format__mutmut_21, 
    'x_runtime_format__mutmut_22': x_runtime_format__mutmut_22, 
    'x_runtime_format__mutmut_23': x_runtime_format__mutmut_23, 
    'x_runtime_format__mutmut_24': x_runtime_format__mutmut_24, 
    'x_runtime_format__mutmut_25': x_runtime_format__mutmut_25, 
    'x_runtime_format__mutmut_26': x_runtime_format__mutmut_26, 
    'x_runtime_format__mutmut_27': x_runtime_format__mutmut_27, 
    'x_runtime_format__mutmut_28': x_runtime_format__mutmut_28, 
    'x_runtime_format__mutmut_29': x_runtime_format__mutmut_29, 
    'x_runtime_format__mutmut_30': x_runtime_format__mutmut_30, 
    'x_runtime_format__mutmut_31': x_runtime_format__mutmut_31, 
    'x_runtime_format__mutmut_32': x_runtime_format__mutmut_32, 
    'x_runtime_format__mutmut_33': x_runtime_format__mutmut_33, 
    'x_runtime_format__mutmut_34': x_runtime_format__mutmut_34, 
    'x_runtime_format__mutmut_35': x_runtime_format__mutmut_35, 
    'x_runtime_format__mutmut_36': x_runtime_format__mutmut_36, 
    'x_runtime_format__mutmut_37': x_runtime_format__mutmut_37, 
    'x_runtime_format__mutmut_38': x_runtime_format__mutmut_38, 
    'x_runtime_format__mutmut_39': x_runtime_format__mutmut_39, 
    'x_runtime_format__mutmut_40': x_runtime_format__mutmut_40
}

def runtime_format(*args, **kwargs):
    result = _mutmut_trampoline(x_runtime_format__mutmut_orig, x_runtime_format__mutmut_mutants, *args, **kwargs)
    return result 

runtime_format.__signature__ = _mutmut_signature(x_runtime_format__mutmut_orig)
x_runtime_format__mutmut_orig.__name__ = 'x_runtime_format'


