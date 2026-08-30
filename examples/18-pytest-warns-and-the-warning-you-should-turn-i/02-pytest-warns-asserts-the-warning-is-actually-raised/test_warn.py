import warnings
import pytest

def old_api():
    warnings.warn('old_api is deprecated', DeprecationWarning)
    return 42

def new_api():
    return 42

def test_warns():
    with pytest.warns(DeprecationWarning, match='deprecated'):
        old_api()

def test_new_does_not_warn():
    with pytest.warns(DeprecationWarning):
        new_api()
