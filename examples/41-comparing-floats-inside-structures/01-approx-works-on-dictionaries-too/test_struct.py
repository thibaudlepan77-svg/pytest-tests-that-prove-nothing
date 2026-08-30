import pytest

def shares(total, parts):
    return {k: total * v for k, v in parts.items()}

def test_shares():
    got = shares(1.0, {'a': 1/3, 'b': 2/3})
    assert got == pytest.approx({'a': 0.3333333333333333, 'b': 0.6666666666666666})

def test_sum_is_one():
    got = shares(1.0, {'a': 1/3, 'b': 2/3})
    assert sum(got.values()) == pytest.approx(1.0)
