import pytest

@pytest.fixture(scope='module')
def counter():
    print('FIXTURE BODY RAN')
    return {'n': 0}

def test_a(counter):
    counter['n'] += 1
    assert counter['n'] == 1

def test_b(counter):
    counter['n'] += 1
    assert counter['n'] == 1
