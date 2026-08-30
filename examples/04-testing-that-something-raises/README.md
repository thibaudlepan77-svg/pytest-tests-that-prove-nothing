# Testing that something raises

3 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `raises`, `match`.

## A try except in a test hides the failure

`test_raises.py`

```python
def divide(a, b):
    return a / b

def test_bad_way():
    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass
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

test_raises.py::test_bad_way PASSED                                      [100%]

============================== 1 passed in 0.01s ==============================
```

## pytest.raises fails loudly when nothing is raised

`test_raises.py`

```python
import pytest

def divide(a, b):
    if b == 0:
        return float('inf')
    return a / b

def test_good_way():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
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

test_raises.py F                                                         [100%]

================================== FAILURES ===================================
________________________________ test_good_way ________________________________

    def test_good_way():
>       with pytest.raises(ZeroDivisionError):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       Failed: DID NOT RAISE ZeroDivisionError

test_raises.py:9: Failed
=========================== short test summary info ===========================
FAILED test_raises.py::test_good_way - Failed: DID NOT RAISE ZeroDivisionError
============================== 1 failed in 0.01s ==============================
```

## match pins the message, not just the type

`test_raises.py`

```python
import pytest

def load(name):
    raise ValueError('unknown format: parquet')

def test_message():
    with pytest.raises(ValueError, match='unknown format'):
        load('x')

def test_wrong_message():
    with pytest.raises(ValueError, match='file not found'):
        load('x')
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

test_raises.py::test_message PASSED                                      [ 50%]
test_raises.py::test_wrong_message FAILED                                [100%]

================================== FAILURES ===================================
_____________________________ test_wrong_message ______________________________

    def test_wrong_message():
>       with pytest.raises(ValueError, match='file not found'):
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AssertionError: Regex pattern did not match.
E         Expected regex: 'file not found'
E         Actual message: 'unknown format: parquet'

test_raises.py:11: AssertionError
=========================== short test summary info ===========================
FAILED test_raises.py::test_wrong_message - AssertionError: Regex pattern did...
========================= 1 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
