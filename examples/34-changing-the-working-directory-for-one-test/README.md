# Changing the working directory for one test

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## monkeypatch.chdir moves you, and moves you back

`test_cwd.py`

```python
import os
from pathlib import Path

def find_config():
    return Path('settings.txt').exists()

def test_finds_it(tmp_path, monkeypatch):
    (tmp_path / 'settings.txt').write_text('x', encoding='utf-8')
    monkeypatch.chdir(tmp_path)
    assert find_config() is True

def test_back_where_we_started():
    assert find_config() is False
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

test_cwd.py::test_finds_it PASSED                                        [ 50%]
test_cwd.py::test_back_where_we_started PASSED                           [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
