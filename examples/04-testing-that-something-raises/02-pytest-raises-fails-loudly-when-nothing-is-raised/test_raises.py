import pytest

def divide(a, b):
    if b == 0:
        return float('inf')
    return a / b

def test_good_way():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
