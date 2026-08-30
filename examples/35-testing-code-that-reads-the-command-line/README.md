# Testing code that reads the command line

1 example. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

Covered here, `setattr`, `args`.

## Patch sys.argv rather than restructuring your program

`cli.py`

```python
import sys

def main():
    args = sys.argv[1:]
    if not args:
        return 'usage: cli NAME'
    return 'hello ' + args[0]
```

`test_cli.py`

```python
import sys
import cli

def test_with_name(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['cli', 'Ada'])
    assert cli.main() == 'hello Ada'

def test_without_name(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['cli'])
    assert cli.main() == 'usage: cli NAME'
```

```bash
pytest -v
```

```output
============================= test session starts =============================
platform linux -- Python 3.13, pytest-9.1, pluggy-1.6
rootdir: /project
plugins: anyio-4.13.0
collecting ... collected 2 items

test_cli.py::test_with_name PASSED                                       [ 50%]
test_cli.py::test_without_name PASSED                                    [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
