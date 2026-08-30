import pytest

@pytest.mark.slow
def test_declared():
    assert True

@pytest.mark.slwo
def test_typo():
    assert True
