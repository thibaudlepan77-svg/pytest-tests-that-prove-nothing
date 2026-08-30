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
