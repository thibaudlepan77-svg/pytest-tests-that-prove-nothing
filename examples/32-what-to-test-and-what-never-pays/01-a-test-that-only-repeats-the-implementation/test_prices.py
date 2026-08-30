from prices import with_tax, TAX

def test_mirrors_the_code():
    assert with_tax(100) == 100 * (1 + TAX)

def test_states_the_answer():
    assert with_tax(100) == 120.0
