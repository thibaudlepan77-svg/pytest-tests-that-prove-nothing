# Stacking parametrize, and the matrix it builds

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Two decorators multiply, they do not zip

`test_matrix.py`

```python
import pytest

@pytest.mark.parametrize('b', [10, 20])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_pairs(a, b):
    assert a * b > 0
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 6 items

test_matrix.py::test_pairs[1-10] PASSED                                  [ 16%]
test_matrix.py::test_pairs[1-20] PASSED                                  [ 33%]
test_matrix.py::test_pairs[2-10] PASSED                                  [ 50%]
test_matrix.py::test_pairs[2-20] PASSED                                  [ 66%]
test_matrix.py::test_pairs[3-10] PASSED                                  [ 83%]
test_matrix.py::test_pairs[3-20] PASSED                                  [100%]

============================== 6 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
