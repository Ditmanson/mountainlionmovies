
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


# Generated by Django 5.1.2 on 2024-11-13 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filmproject", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lt_viewer_cosine_similarity",
            name="cosine_similarity",
            field=models.DecimalField(
                decimal_places=4, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="lt_viewer_cosine_similarity",
            name="viewer_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="viewer_1",
                to="filmproject.viewer",
            ),
        ),
        migrations.AlterField(
            model_name="lt_viewer_cosine_similarity",
            name="viewer_2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="viewer_2",
                to="filmproject.viewer",
            ),
        ),
        migrations.AddIndex(
            model_name="lt_viewer_cosine_similarity",
            index=models.Index(
                fields=["viewer_1", "viewer_2"],
                name="filmproject_viewer__b16745_idx",
            ),
        ),
    ]
