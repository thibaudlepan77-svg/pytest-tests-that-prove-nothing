# What a green suite does not prove

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Every line runs, and the bug still ships

`discount.py`

```python
def price(amount, member):
    if member:
        amount = amount * 0.9
    return round(amount, 2)
```

`test_discount.py`

```python
from discount import price

def test_member():
    assert price(100, True) == 90.0

def test_non_member():
    assert price(100, False) == 100.0
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

test_discount.py::test_member PASSED                                     [ 50%]
test_discount.py::test_non_member PASSED                                 [100%]

============================== 2 passed in 0.01s ==============================
```

## The case nobody wrote a test for

`discount.py`

```python
def price(amount, member):
    if member:
        amount = amount * 0.9
    return round(amount, 2)
```

`test_discount.py`

```python
from discount import price

def test_negative_amount_is_refused():
    assert price(-100, True) >= 0
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

test_discount.py::test_negative_amount_is_refused FAILED                 [100%]

================================== FAILURES ===================================
_______________________ test_negative_amount_is_refused _______________________

    def test_negative_amount_is_refused():
>       assert price(-100, True) >= 0
E       assert -90.0 >= 0
E        +  where -90.0 = price(-100, True)

test_discount.py:4: AssertionError
=========================== short test summary info ===========================
FAILED test_discount.py::test_negative_amount_is_refused - assert -90.0 >= 0
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
