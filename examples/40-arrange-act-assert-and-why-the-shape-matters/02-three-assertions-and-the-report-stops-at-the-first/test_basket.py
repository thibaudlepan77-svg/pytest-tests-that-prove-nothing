from basket import total

def test_everything_at_once():
    assert total([]) == 0
    assert total([{'price': 1.0, 'qty': 1}], discount=0.5) == 0.6
    assert total([{'price': 1.0, 'qty': 3}]) == 3.0
