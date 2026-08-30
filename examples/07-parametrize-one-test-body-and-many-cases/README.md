# Parametrize, one test body and many cases

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## Each case is a separate test with its own name

`test_param.py`

```python
import pytest

def slugify(s):
    return s.strip().lower().replace(' ', '-')

@pytest.mark.parametrize('raw,expected', [
    ('Hello World', 'hello-world'),
    ('  padded  ', 'padded'),
    ('UPPER', 'upper'),
    ('two  spaces', 'two-spaces'),
])
def test_slugify(raw, expected):
    assert slugify(raw) == expected
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 4 items

test_param.py::test_slugify[Hello World-hello-world] PASSED              [ 25%]
test_param.py::test_slugify[  padded  -padded] PASSED                    [ 50%]
test_param.py::test_slugify[UPPER-upper] PASSED                          [ 75%]
test_param.py::test_slugify[two  spaces-two-spaces] FAILED               [100%]

================================== FAILURES ===================================
____________________ test_slugify[two  spaces-two-spaces] _____________________

raw = 'two  spaces', expected = 'two-spaces'

    @pytest.mark.parametrize('raw,expected', [
        ('Hello World', 'hello-world'),
        ('  padded  ', 'padded'),
        ('UPPER', 'upper'),
        ('two  spaces', 'two-spaces'),
    ])
    def test_slugify(raw, expected):
>       assert slugify(raw) == expected
E       AssertionError: assert 'two--spaces' == 'two-spaces'
E         
E         - two-spaces
E         + two--spaces
E         ?    +

test_param.py:13: AssertionError
=========================== short test summary info ===========================
FAILED test_param.py::test_slugify[two  spaces-two-spaces] - AssertionError: ...
========================= 1 failed, 3 passed in 0.01s =========================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
