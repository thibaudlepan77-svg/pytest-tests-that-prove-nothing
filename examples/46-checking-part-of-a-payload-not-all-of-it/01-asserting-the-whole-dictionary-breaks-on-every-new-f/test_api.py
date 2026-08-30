from api import payload

def test_whole_thing():
    assert payload() == {'id': 7, 'name': 'Ada'}
