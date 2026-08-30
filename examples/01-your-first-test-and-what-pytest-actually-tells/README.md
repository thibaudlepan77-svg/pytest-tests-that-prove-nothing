# Your first test, and what pytest actually tells you

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A passing test says almost nothing

`test_first.py`

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
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

test_first.py::test_add PASSED                                           [100%]

============================== 1 passed in 0.01s ==============================
```

## A failing test shows you the values, not just the line

`test_first.py`

```python
def add(a, b):
    return a - b

def test_add():
    assert add(2, 3) == 5
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

test_first.py::test_add FAILED                                           [100%]

================================== FAILURES ===================================
__________________________________ test_add ___________________________________

    def test_add():
>       assert add(2, 3) == 5
E       assert -1 == 5
E        +  where -1 = add(2, 3)

test_first.py:5: AssertionError
=========================== short test summary info ===========================
FAILED test_first.py::test_add - assert -1 == 5
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
