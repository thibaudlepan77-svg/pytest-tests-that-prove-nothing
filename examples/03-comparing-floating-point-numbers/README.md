# Comparing floating point numbers

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `approx`.

## Equality on floats fails for reasons that are not your fault

`test_float.py`

```python
def test_naive():
    assert 0.1 + 0.2 == 0.3
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

test_float.py F                                                          [100%]

================================== FAILURES ===================================
_________________________________ test_naive __________________________________

    def test_naive():
>       assert 0.1 + 0.2 == 0.3
E       assert (0.1 + 0.2) == 0.3

test_float.py:2: AssertionError
=========================== short test summary info ===========================
FAILED test_float.py::test_naive - assert (0.1 + 0.2) == 0.3
============================== 1 failed in 0.01s ==============================
```

## pytest.approx is the fix, and it is one import

`test_float.py`

```python
import pytest

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_approx_list():
    assert [0.1 + 0.2, 1 / 3] == pytest.approx([0.3, 0.3333333333333333])
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

test_float.py::test_approx PASSED                                        [ 50%]
test_float.py::test_approx_list PASSED                                   [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
