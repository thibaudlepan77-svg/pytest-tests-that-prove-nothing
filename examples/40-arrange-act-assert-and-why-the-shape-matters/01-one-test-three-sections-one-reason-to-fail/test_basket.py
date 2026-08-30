from basket import total

def test_applies_discount():
    items = [{'price': 10.0, 'qty': 2}, {'price': 5.0, 'qty': 1}]

    got = total(items, discount=0.1)

    assert got == 22.5
