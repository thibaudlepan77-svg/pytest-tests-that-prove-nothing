import pytest
from loader import load, LoadError

def test_raises_load_error():
    with pytest.raises(LoadError):
        load('abc')

def test_keeps_the_cause():
    with pytest.raises(LoadError) as info:
        load('abc')
    assert isinstance(info.value.__cause__, ValueError)
