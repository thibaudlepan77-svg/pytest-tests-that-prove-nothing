import pytest
from account import withdraw, InsufficientFunds

@pytest.mark.parametrize('balance,amount,expected', [
    (100.0, 30.0, 70.0),
    (100.0, 100.0, 0.0),
    (0.1, 0.05, 0.05),
], ids=['partial', 'exact', 'small-floats'])
def test_withdraw(balance, amount, expected):
    assert withdraw(balance, amount) == pytest.approx(expected)

def test_refuses_too_much():
    with pytest.raises(InsufficientFunds, match='balance is 50'):
        withdraw(50.0, 80.0)

@pytest.mark.parametrize('bad', [0, -5], ids=['zero', 'negative'])
def test_refuses_bad_amount(bad):
    with pytest.raises(ValueError):
        withdraw(100.0, bad)
