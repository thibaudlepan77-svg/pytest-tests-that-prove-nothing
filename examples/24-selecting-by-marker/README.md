# Selecting by marker

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## -m runs only the tests carrying the mark

`pytest.ini`

```python
[pytest]
markers =
    slow: takes more than a second
```

`test_sel.py`

```python
import pytest

@pytest.mark.slow
def test_big_import():
    assert True

def test_fast_one():
    assert True

def test_fast_two():
    assert True
```

```bash
pytest -v -m not slow
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
configfile: pytest.ini
plugins: anyio-4.13.0
collecting ... collected 3 items / 1 deselected / 2 selected

test_sel.py::test_fast_one PASSED                                        [ 50%]
test_sel.py::test_fast_two PASSED                                        [100%]

======================= 2 passed, 1 deselected in 0.01s =======================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
