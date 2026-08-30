# What to test, and what never pays

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A test that only repeats the implementation

`prices.py`

```python
TAX = 0.2

def with_tax(amount):
    return amount * (1 + TAX)
```

`test_prices.py`

```python
from prices import with_tax, TAX

def test_mirrors_the_code():
    assert with_tax(100) == 100 * (1 + TAX)

def test_states_the_answer():
    assert with_tax(100) == 120.0
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

test_prices.py::test_mirrors_the_code PASSED                             [ 50%]
test_prices.py::test_states_the_answer PASSED                            [100%]

============================== 2 passed in 0.01s ==============================
```

## Change the constant, and only one test notices

`prices.py`

```python
TAX = 0.25

def with_tax(amount):
    return amount * (1 + TAX)
```

`test_prices.py`

```python
from prices import with_tax, TAX

def test_mirrors_the_code():
    assert with_tax(100) == 100 * (1 + TAX)

def test_states_the_answer():
    assert with_tax(100) == 120.0
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

test_prices.py::test_mirrors_the_code PASSED                             [ 50%]
test_prices.py::test_states_the_answer FAILED                            [100%]

================================== FAILURES ===================================
___________________________ test_states_the_answer ____________________________

    def test_states_the_answer():
>       assert with_tax(100) == 120.0
E       assert 125.0 == 120.0
E        +  where 125.0 = with_tax(100)

test_prices.py:7: AssertionError
=========================== short test summary info ===========================
FAILED test_prices.py::test_states_the_answer - assert 125.0 == 120.0
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
