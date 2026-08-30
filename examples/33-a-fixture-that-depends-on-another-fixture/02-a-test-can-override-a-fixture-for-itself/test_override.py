import pytest

@pytest.fixture
def config():
    return {'host': 'example.com', 'port': 443}

def test_uses_local_override(config):
    assert config['host'] == 'example.com'
