import warnings

def old_api():
    warnings.warn('old_api is deprecated', DeprecationWarning)
    return 42

def test_still_works():
    assert old_api() == 42
