import pytest
from stock import take, OutOfStock

@pytest.fixture
def stock():
    return {'apple': 3}

def test_takes_and_returns_remaining(stock):
    assert take(stock, 'apple', 2) == 1

def test_refuses_more_than_available(stock):
    with pytest.raises(OutOfStock, match='apple'):
        take(stock, 'apple', 4)

def test_stock_untouched_after_failure(stock):
    with pytest.raises(OutOfStock):
        take(stock, 'apple', 4)
    assert stock['apple'] == 3

@pytest.mark.parametrize('n', [0, -1], ids=['zero', 'negative'])
def test_refuses_bad_quantity(stock, n):
    with pytest.raises(ValueError):
        take(stock, 'apple', n)
