import pytest

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_approx_list():
    assert [0.1 + 0.2, 1 / 3] == pytest.approx([0.3, 0.3333333333333333])
