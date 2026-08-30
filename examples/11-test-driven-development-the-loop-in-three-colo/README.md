# Test driven development, the loop in three colours

3 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `raises`, `amount`, `currency`.

## Red, the test exists before the code does

`test_tdd.py`

```python
from money import Money

def test_add_same_currency():
    assert Money(5, 'EUR') + Money(3, 'EUR') == Money(8, 'EUR')
```

`money.py`

```python
class Money:
    pass
```

```bash
pytest 
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 1 item

test_tdd.py F                                                            [100%]

================================== FAILURES ===================================
___________________________ test_add_same_currency ____________________________

    def test_add_same_currency():
>       assert Money(5, 'EUR') + Money(3, 'EUR') == Money(8, 'EUR')
               ^^^^^^^^^^^^^^^
E       TypeError: Money() takes no arguments

test_tdd.py:4: TypeError
=========================== short test summary info ===========================
FAILED test_tdd.py::test_add_same_currency - TypeError: Money() takes no argu...
============================== 1 failed in 0.01s ==============================
```

## Green, the smallest code that passes

`test_tdd.py`

```python
from money import Money

def test_add_same_currency():
    assert Money(5, 'EUR') + Money(3, 'EUR') == Money(8, 'EUR')
```

`money.py`

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return (self.amount, self.currency) == (other.amount, other.currency)
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_tdd.py::test_add_same_currency PASSED                               [100%]

============================== 1 passed in 0.01s ==============================
```

## The next red, written the moment you think of the case

`test_tdd.py`

```python
import pytest
from money import Money

def test_add_same_currency():
    assert Money(5, 'EUR') + Money(3, 'EUR') == Money(8, 'EUR')

def test_refuses_mixed_currency():
    with pytest.raises(ValueError):
        Money(5, 'EUR') + Money(3, 'USD')
```

`money.py`

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):
        return (self.amount, self.currency) == (other.amount, other.currency)
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 2 items

test_tdd.py::test_add_same_currency PASSED                               [ 50%]
test_tdd.py::test_refuses_mixed_currency FAILED                          [100%]

================================== FAILURES ===================================
_________________________ test_refuses_mixed_currency _________________________

    def test_refuses_mixed_currency():
>       with pytest.raises(ValueError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ValueError

test_tdd.py:8: Failed
=========================== short test summary info ===========================
FAILED test_tdd.py::test_refuses_mixed_currency - Failed: DID NOT RAISE Value...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
