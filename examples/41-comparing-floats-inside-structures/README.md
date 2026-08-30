# Comparing floats inside structures

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## approx works on dictionaries too

`test_struct.py`

```python
import pytest

def shares(total, parts):
    return {k: total * v for k, v in parts.items()}

def test_shares():
    got = shares(1.0, {'a': 1/3, 'b': 2/3})
    assert got == pytest.approx({'a': 0.3333333333333333, 'b': 0.6666666666666666})

def test_sum_is_one():
    got = shares(1.0, {'a': 1/3, 'b': 2/3})
    assert sum(got.values()) == pytest.approx(1.0)
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

test_struct.py::test_shares PASSED                                       [ 50%]
test_struct.py::test_sum_is_one PASSED                                   [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
