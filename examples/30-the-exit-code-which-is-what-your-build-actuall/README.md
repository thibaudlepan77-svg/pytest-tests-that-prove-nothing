# The exit code, which is what your build actually reads

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Zero when everything passes

`test_exit.py`

```python
def test_ok():
    assert True
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

test_exit.py .                                                           [100%]

============================== 1 passed in 0.01s ==============================
```

## Five when nothing was collected, and that is the dangerous one

`test_typo_name.py`

```python
def check_ok():
    assert True
```

```bash
pytest 
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 0 items

============================ no tests ran in 0.01s ============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
