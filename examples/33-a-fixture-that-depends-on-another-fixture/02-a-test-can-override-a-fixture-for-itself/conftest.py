import pytest

@pytest.fixture
def config():
    return {'host': 'localhost', 'port': 5432}
