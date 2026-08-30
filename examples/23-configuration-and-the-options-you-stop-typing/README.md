# Configuration, and the options you stop typing

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## addopts applies to every run in the project

`pytest.ini`

```python
[pytest]
addopts = -v --strict-markers
testpaths = tests
```

`tests/test_conf.py`

```python
def test_one():
    assert True

def test_two():
    assert True
```

```bash
pytest 
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.13.0
collecting ... collected 2 items

tests/test_conf.py::test_one PASSED                                      [ 50%]
tests/test_conf.py::test_two PASSED                                      [100%]

============================== 2 passed in 0.01s ==============================
```

## strict-markers turns a typo into a failure

`pytest.ini`

```python
[pytest]
addopts = --strict-markers
markers =
    slow: takes more than a second
```

`test_marks.py`

```python
import pytest

@pytest.mark.slow
def test_declared():
    assert True

@pytest.mark.slwo
def test_typo():
    assert True
```

```bash
pytest 
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
configfile: pytest.ini
plugins: anyio-4.13.0
collected 0 items / 1 error

=================================== ERRORS ====================================
_______________________ ERROR collecting test_marks.py ________________________
'slwo' not found in `markers` configuration option
=========================== short test summary info ===========================
ERROR test_marks.py - Failed: 'slwo' not found in `markers` configuration option
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.01s ===============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
