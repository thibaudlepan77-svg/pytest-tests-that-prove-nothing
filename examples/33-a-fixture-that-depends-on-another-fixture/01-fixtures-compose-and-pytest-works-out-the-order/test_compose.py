import pytest

@pytest.fixture
def config():
    print('BUILD config')
    return {'host': 'localhost', 'port': 5432}

@pytest.fixture
def client(config):
    print('BUILD client')
    return {'url': config['host'] + ':' + str(config['port'])}

def test_url(client):
    assert client['url'] == 'localhost:5432'
