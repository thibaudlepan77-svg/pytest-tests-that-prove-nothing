CACHE = {}

def test_writes():
    CACHE['user'] = 'Ada'
    assert CACHE['user'] == 'Ada'

def test_expects_empty():
    assert CACHE == {}
