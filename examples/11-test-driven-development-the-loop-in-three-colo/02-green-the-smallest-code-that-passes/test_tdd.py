from money import Money

def test_add_same_currency():
    assert Money(5, 'EUR') + Money(3, 'EUR') == Money(8, 'EUR')
