import pytest

def vat(amount, country):
    rates = {'FR': 0.20, 'DE': 0.19, 'JP': 0.10}
    return round(amount * (1 + rates[country]), 2)

@pytest.mark.parametrize('amount,country,expected', [
    (100, 'FR', 120.0),
    (100, 'DE', 119.0),
    (100, 'JP', 110.0),
])
def test_vat(amount, country, expected):
    assert vat(amount, country) == expected
