# Failing fast, and rerunning only what broke

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## -x stops at the first failure

`test_fast.py`

```python
def test_a():
    assert True

def test_b():
    assert 1 == 2

def test_c():
    assert 1 == 3

def test_d():
    assert True
```

```bash
pytest -v -x
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 4 items

test_fast.py::test_a PASSED                                              [ 25%]
test_fast.py::test_b FAILED                                              [ 50%]

================================== FAILURES ===================================
___________________________________ test_b ____________________________________

    def test_b():
>       assert 1 == 2
E       assert 1 == 2

test_fast.py:5: AssertionError
=========================== short test summary info ===========================
FAILED test_fast.py::test_b - assert 1 == 2
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!
========================= 1 failed, 1 passed in 0.01s =========================
```

## --maxfail gives you a budget instead of a cliff

`test_fast.py`

```python
def test_a():
    assert True

def test_b():
    assert 1 == 2

def test_c():
    assert 1 == 3

def test_d():
    assert True
```

```bash
pytest -v --maxfail=2
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 4 items

test_fast.py::test_a PASSED                                              [ 25%]
test_fast.py::test_b FAILED                                              [ 50%]
test_fast.py::test_c FAILED                                              [ 75%]

================================== FAILURES ===================================
___________________________________ test_b ____________________________________

    def test_b():
>       assert 1 == 2
E       assert 1 == 2

test_fast.py:5: AssertionError
___________________________________ test_c ____________________________________

    def test_c():
>       assert 1 == 3
E       assert 1 == 3

test_fast.py:8: AssertionError
=========================== short test summary info ===========================
FAILED test_fast.py::test_b - assert 1 == 2
FAILED test_fast.py::test_c - assert 1 == 3
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 2 failures !!!!!!!!!!!!!!!!!!!!!!!!!!
========================= 2 failed, 1 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
