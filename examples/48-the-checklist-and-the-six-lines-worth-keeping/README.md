# The checklist, and the six lines worth keeping

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Everything this course argues for, in one file

`account.py`

```python
class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError('amount must be positive')
    if amount > balance:
        raise InsufficientFunds('balance is ' + str(balance))
    return round(balance - amount, 2)
```

`test_account.py`

```python
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
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 6 items

test_account.py::test_withdraw[partial] PASSED                           [ 16%]
test_account.py::test_withdraw[exact] PASSED                             [ 33%]
test_account.py::test_withdraw[small-floats] PASSED                      [ 50%]
test_account.py::test_refuses_too_much PASSED                            [ 66%]
test_account.py::test_refuses_bad_amount[zero] PASSED                    [ 83%]
test_account.py::test_refuses_bad_amount[negative] PASSED                [100%]

============================== 6 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
