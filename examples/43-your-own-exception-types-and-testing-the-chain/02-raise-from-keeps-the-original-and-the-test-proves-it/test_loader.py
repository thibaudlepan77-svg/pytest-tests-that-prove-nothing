import pytest
from loader import load, LoadError

def test_keeps_the_cause():
    with pytest.raises(LoadError) as info:
        load('abc')
    assert isinstance(info.value.__cause__, ValueError)
    assert 'abc' in str(info.value.__cause__)
