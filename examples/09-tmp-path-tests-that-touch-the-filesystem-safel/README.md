# tmp_path, tests that touch the filesystem safely

1 examples. Every block below is a real pytest run on pytest 9.1 and
Python 3.13, captured automatically.

## tmp_path gives every test a private directory

`test_files.py`

```python
def save(path, text):
    path.write_text(text, encoding='utf-8')
    return path

def test_writes(tmp_path):
    f = save(tmp_path / 'out.txt', 'hello')
    assert f.read_text(encoding='utf-8') == 'hello'

def test_starts_empty(tmp_path):
    assert list(tmp_path.iterdir()) == []
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

test_files.py::test_writes PASSED                                        [ 50%]
test_files.py::test_starts_empty PASSED                                  [100%]

============================== 2 passed in 0.01s ==============================
```

---

Part of [pytest, tests that pass and prove nothing](../..), 85
examples. `verifier.py` at the root re-runs every one of them.
