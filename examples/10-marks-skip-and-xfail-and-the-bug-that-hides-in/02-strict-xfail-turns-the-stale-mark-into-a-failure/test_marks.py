import pytest

@pytest.mark.xfail(reason='fixed last week', strict=True)
def test_already_fixed():
    assert 1 == 1
