import pytest

@pytest.fixture(scope='session')
def heavy():
    print('EXPENSIVE SETUP')
    return {'rows': 1000}

@pytest.fixture
def rows(heavy):
    return dict(heavy)
