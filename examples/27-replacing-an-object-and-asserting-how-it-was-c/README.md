# Replacing an object, and asserting how it was called

2 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## A fake records the calls, so you can assert on them

`mailer.py`

```python
def send(to, subject):
    raise RuntimeError('this would really send an email')
```

`signup.py`

```python
import mailer

def register(email):
    mailer.send(email, 'Welcome')
    return {'email': email}
```

`test_signup.py`

```python
import signup

def test_sends_welcome(monkeypatch):
    calls = []
    monkeypatch.setattr(signup.mailer, 'send',
                        lambda to, subject: calls.append((to, subject)))
    signup.register('ada@example.com')
    assert calls == [('ada@example.com', 'Welcome')]
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

test_signup.py::test_sends_welcome PASSED                                [100%]

============================== 1 passed in 0.01s ==============================
```

## Without the fake, the test hits the real thing

`mailer.py`

```python
def send(to, subject):
    raise RuntimeError('this would really send an email')
```

`signup.py`

```python
import mailer

def register(email):
    mailer.send(email, 'Welcome')
    return {'email': email}
```

`test_signup.py`

```python
import signup

def test_no_fake():
    signup.register('ada@example.com')
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

test_signup.py F                                                         [100%]

================================== FAILURES ===================================
________________________________ test_no_fake _________________________________

    def test_no_fake():
>       signup.register('ada@example.com')

test_signup.py:4: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
signup.py:4: in register
    mailer.send(email, 'Welcome')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

to = 'ada@example.com', subject = 'Welcome'

    def send(to, subject):
>       raise RuntimeError('this would really send an email')
E       RuntimeError: this would really send an email

mailer.py:2: RuntimeError
=========================== short test summary info ===========================
FAILED test_signup.py::test_no_fake - RuntimeError: this would really send an...
============================== 1 failed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
