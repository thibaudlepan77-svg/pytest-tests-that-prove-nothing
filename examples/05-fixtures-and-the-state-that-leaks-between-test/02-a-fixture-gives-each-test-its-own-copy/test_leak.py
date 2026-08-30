import pytest

@pytest.fixture
def items():
    return []

def test_one(items):
    items.append('a')
    assert len(items) == 1

def test_two(items):
    items.append('b')
    assert len(items) == 1
