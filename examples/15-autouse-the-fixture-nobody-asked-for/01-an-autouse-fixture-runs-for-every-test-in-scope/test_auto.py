import pytest

STATE = {'calls': 0}

@pytest.fixture(autouse=True)
def reset():
    STATE['calls'] = 0

def test_a():
    STATE['calls'] += 1
    assert STATE['calls'] == 1

def test_b():
    STATE['calls'] += 1
    assert STATE['calls'] == 1
