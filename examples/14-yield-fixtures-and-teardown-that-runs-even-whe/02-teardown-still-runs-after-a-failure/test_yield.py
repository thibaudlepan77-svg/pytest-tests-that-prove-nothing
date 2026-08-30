import pytest

@pytest.fixture
def connection():
    print('OPEN')
    yield {'open': True}
    print('CLOSE')

def test_fails(connection):
    print('TEST BODY')
    assert connection['open'] is False
