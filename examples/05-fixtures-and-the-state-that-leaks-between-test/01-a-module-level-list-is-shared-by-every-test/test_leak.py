ITEMS = []

def test_one():
    ITEMS.append('a')
    assert len(ITEMS) == 1

def test_two():
    ITEMS.append('b')
    assert len(ITEMS) == 1
