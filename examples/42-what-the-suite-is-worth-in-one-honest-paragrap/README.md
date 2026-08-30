# What the suite is worth, in one honest paragraph

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## The final shape, everything in one file

`stock.py`

```python
class OutOfStock(Exception):
    pass

def take(stock, item, n):
    if n <= 0:
        raise ValueError('n must be positive')
    if stock.get(item, 0) < n:
        raise OutOfStock(item)
    stock[item] -= n
    return stock[item]
```

`test_stock.py`

```python
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
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 5 items

test_stock.py::test_takes_and_returns_remaining PASSED                   [ 20%]
test_stock.py::test_refuses_more_than_available PASSED                   [ 40%]
test_stock.py::test_stock_untouched_after_failure PASSED                 [ 60%]
test_stock.py::test_refuses_bad_quantity[zero] PASSED                    [ 80%]
test_stock.py::test_refuses_bad_quantity[negative] PASSED                [100%]

============================== 5 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
