# The test that passes and proves nothing

3 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A test with no assert always passes

`test_silent.py`

```python
def divide(a, b):
    return a / b

def test_divide():
    divide(10, 2)
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

test_silent.py::test_divide PASSED                                       [100%]

============================== 1 passed in 0.01s ==============================
```

## A tautology passes forever, whatever the code does

`test_silent.py`

```python
def divide(a, b):
    return a / b

def test_divide():
    result = divide(10, 2)
    assert result == result
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

test_silent.py::test_divide PASSED                                       [100%]

============================== 1 passed in 0.01s ==============================
```

## An assert on a tuple is always true

`test_silent.py`

```python
def test_tuple_trap():
    assert (1 == 2, 'this message never prints')
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

test_silent.py::test_tuple_trap PASSED                                   [100%]

============================== warnings summary ===============================
test_silent.py:2
  /test_silent.py:2: PytestAssertRewriteWarning: assertion is always true, perhaps remove parentheses?
    assert (1 == 2, 'this message never prints')

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 1 passed, 1 warning in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
