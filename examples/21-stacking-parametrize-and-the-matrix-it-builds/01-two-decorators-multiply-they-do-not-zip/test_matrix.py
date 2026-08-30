import pytest

@pytest.mark.parametrize('b', [10, 20])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_pairs(a, b):
    assert a * b > 0
