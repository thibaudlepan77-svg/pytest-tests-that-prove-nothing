from discount import price

def test_member():
    assert price(100, True) == 90.0

def test_non_member():
    assert price(100, False) == 100.0
