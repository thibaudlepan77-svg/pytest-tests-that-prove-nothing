# Running only part of the suite

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## -k selects by expression on the test name

`test_sel.py`

```python
def test_login_ok():
    assert True

def test_login_fails():
    assert True

def test_logout():
    assert True
```

```bash
pytest -v -k login and not fails
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 3 items / 2 deselected / 1 selected

test_sel.py::test_login_ok PASSED                                        [100%]

======================= 1 passed, 2 deselected in 0.01s =======================
```

## A node id runs exactly one test

`test_sel.py`

```python
def test_login_ok():
    assert True

def test_login_fails():
    assert True

def test_logout():
    assert True
```

```bash
pytest -v test_sel.py::test_logout
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 1 item

test_sel.py::test_logout PASSED                                          [100%]

============================== 1 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
