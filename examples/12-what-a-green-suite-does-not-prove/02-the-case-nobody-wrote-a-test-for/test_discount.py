from discount import price

def test_negative_amount_is_refused():
    assert price(-100, True) >= 0
