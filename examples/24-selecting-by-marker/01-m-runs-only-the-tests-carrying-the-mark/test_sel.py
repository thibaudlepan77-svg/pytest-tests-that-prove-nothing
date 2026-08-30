import pytest

@pytest.mark.slow
def test_big_import():
    assert True

def test_fast_one():
    assert True

def test_fast_two():
    assert True
