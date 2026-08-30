# capsys, testing what a function prints

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `readouterr`, `err`, `first`, `second`.

## capsys captures stdout so you can assert on it

`test_print.py`

```python
def greet(name):
    print('Hello, ' + name)

def test_greet(capsys):
    greet('Ada')
    out, err = capsys.readouterr()
    assert out == 'Hello, Ada\n'
    assert err == ''
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

test_print.py::test_greet PASSED                                         [100%]

============================== 1 passed in 0.01s ==============================
```

## readouterr empties the buffer, which surprises people once

`test_print.py`

```python
def greet(name):
    print('Hello, ' + name)

def test_twice(capsys):
    greet('Ada')
    first = capsys.readouterr().out
    second = capsys.readouterr().out
    assert first == 'Hello, Ada\n'
    assert second == 'Hello, Ada\n'
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

test_print.py::test_twice FAILED                                         [100%]

================================== FAILURES ===================================
_________________________________ test_twice __________________________________

capsys = <_pytest.capture.CaptureFixture object at 0x0000028DE472C2F0>

    def test_twice(capsys):
        greet('Ada')
        first = capsys.readouterr().out
        second = capsys.readouterr().out
        assert first == 'Hello, Ada/n'
>       assert second == 'Hello, Ada/n'
E       AssertionError: assert '' == 'Hello, Ada/n'
E         
E         - Hello, Ada

test_print.py:9: AssertionError
=========================== short test summary info ===========================
FAILED test_print.py::test_twice - AssertionError: assert '' == 'Hello, Ada/n'
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
