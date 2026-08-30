import pytest

@pytest.fixture
def customer():
    return {'id': 1, 'name': 'Ada', 'credit': 100}
