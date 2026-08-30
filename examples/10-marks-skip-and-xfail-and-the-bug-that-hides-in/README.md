# Marks, skip and xfail, and the bug that hides in them

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `xfail`, `skip`, `reason`, `strict`, `mark`.

## xfail passes when the test fails, and warns when it does not

`test_marks.py`

```python
import pytest

@pytest.mark.xfail(reason='known bug, ticket 412')
def test_known_bug():
    assert 1 == 2

@pytest.mark.xfail(reason='fixed last week, nobody removed the mark')
def test_already_fixed():
    assert 1 == 1

@pytest.mark.skip(reason='needs a database')
def test_skipped():
    assert False
```

```bash
pytest -v -rxXs
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 3 items

test_marks.py::test_known_bug XFAIL (known bug, ticket 412)              [ 33%]
test_marks.py::test_already_fixed XPASS (fixed last week, nobody rem...) [ 66%]
test_marks.py::test_skipped SKIPPED (needs a database)                   [100%]

=================================== XPASSES ===================================
=========================== short test summary info ===========================
XFAIL test_marks.py::test_known_bug - known bug, ticket 412
XPASS test_marks.py::test_already_fixed - fixed last week, nobody removed the mark
SKIPPED [1] test_marks.py:11: needs a database
================== 1 skipped, 1 xfailed, 1 xpassed in 0.01s ===================
```

## strict xfail turns the stale mark into a failure

`test_marks.py`

```python
import pytest

@pytest.mark.xfail(reason='fixed last week', strict=True)
def test_already_fixed():
    assert 1 == 1
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

test_marks.py::test_already_fixed FAILED                                 [100%]

================================== FAILURES ===================================
_____________________________ test_already_fixed ______________________________
[XPASS(strict)] fixed last week
=========================== short test summary info ===========================
FAILED test_marks.py::test_already_fixed - [XPASS(strict)] fixed last week
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
