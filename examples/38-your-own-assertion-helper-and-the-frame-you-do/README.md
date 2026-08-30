# Your own assertion helper, and the frame you do not want

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A helper points the failure at itself

`test_helper.py`

```python
def assert_valid(user):
    assert 'name' in user
    assert user.get('credit', 0) >= 0

def test_user():
    assert_valid({'name': 'Ada', 'credit': -5})
```

```bash
pytest --tb=short
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 1 item

test_helper.py F                                                         [100%]

================================== FAILURES ===================================
__________________________________ test_user __________________________________
test_helper.py:6: in test_user
    assert_valid({'name': 'Ada', 'credit': -5})
test_helper.py:3: in assert_valid
    assert user.get('credit', 0) >= 0
E   AssertionError: assert -5 >= 0
E    +  where -5 = <built-in method get of dict object at 0x000001E956165F00>('credit', 0)
E    +    where <built-in method get of dict object at 0x000001E956165F00> = {'name': 'Ada', 'credit': -5}.get
=========================== short test summary info ===========================
FAILED test_helper.py::test_user - AssertionError: assert -5 >= 0
============================== 1 failed in 0.01s ==============================
```

## __tracebackhide__ points it at the caller instead

`test_helper.py`

```python
def assert_valid(user):
    __tracebackhide__ = True
    assert 'name' in user
    assert user.get('credit', 0) >= 0

def test_user():
    assert_valid({'name': 'Ada', 'credit': -5})
```

```bash
pytest --tb=short
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collected 1 item

test_helper.py F                                                         [100%]

================================== FAILURES ===================================
__________________________________ test_user __________________________________
test_helper.py:7: in test_user
    assert_valid({'name': 'Ada', 'credit': -5})
E   AssertionError: assert -5 >= 0
E    +  where -5 = <built-in method get of dict object at 0x0000027AF06C6000>('credit', 0)
E    +    where <built-in method get of dict object at 0x0000027AF06C6000> = {'name': 'Ada', 'credit': -5}.get
=========================== short test summary info ===========================
FAILED test_helper.py::test_user - AssertionError: assert -5 >= 0
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
