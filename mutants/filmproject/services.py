
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


import pandas as pd
from django.db import transaction
from sklearn.metrics.pairwise import cosine_similarity
from filmproject.models import (
    LT_Viewer_Seen,
    LT_Viewer_Cosine_Similarity,
)


@transaction.atomic
def calculate_cosine_similarity():
    # Step 1: Fetch viewer ratings
    ratings = LT_Viewer_Seen.objects.filter(
        viewer_rating__isnull=False
    ).values("viewer_id", "film_id", "viewer_rating")

    # Step 2: Construct User-Movie matrix
    df = pd.DataFrame(ratings)
    user_movie_matrix = df.pivot_table(
        index="viewer_id",
        columns="film_id",
        values="viewer_rating",
        fill_value=0,
    )

    # Step 3: Compute cosine similarity
    similarity_matrix = cosine_similarity(user_movie_matrix)
    viewers = user_movie_matrix.index.tolist()

    # Step 4: Update the LT_Viewer_Cosine_Similarity table
    for i, viewer_1 in enumerate(viewers):
        for j, viewer_2 in enumerate(viewers):
            if viewer_1 != viewer_2:
                similarity = similarity_matrix[i, j]
                LT_Viewer_Cosine_Similarity.objects.update_or_create(
                    viewer_1_id=viewer_1,
                    viewer_2_id=viewer_2,
                    defaults={"cosine_similarity": round(similarity, 4)},
                )

    print("Cosine similarity calculations complete and saved to the database.")
