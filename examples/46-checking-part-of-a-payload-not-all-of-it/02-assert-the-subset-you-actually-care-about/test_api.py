from api import payload

def test_subset():
    got = payload()
    assert got['id'] == 7
    assert got['name'] == 'Ada'

def test_subset_in_one_line():
    got = payload()
    assert {'id': 7, 'name': 'Ada'}.items() <= got.items()
