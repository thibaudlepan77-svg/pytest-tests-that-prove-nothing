# Skipping for a reason the machine can check

1 example. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `skipif`, `reason`, `mark`.

## skipif evaluates a condition, not a mood

`test_skip.py`

```python
import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3, 8),
                    reason='needs Python 3.8 or later')
def test_modern():
    assert True

@pytest.mark.skipif(sys.version_info >= (3, 8),
                    reason='only for Python 3.7 and older')
def test_legacy():
    assert False
```

```bash
pytest -v -rs
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 2 items

test_skip.py::test_modern PASSED                                         [ 50%]
test_skip.py::test_legacy SKIPPED (only for Python 3.7 and older)        [100%]

=========================== short test summary info ===========================
SKIPPED [1] test_skip.py:9: only for Python 3.7 and older
======================== 1 passed, 1 skipped in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
