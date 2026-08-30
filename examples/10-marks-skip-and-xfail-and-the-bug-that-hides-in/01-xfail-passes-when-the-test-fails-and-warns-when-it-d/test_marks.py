import pytest

@pytest.mark.xfail(reason='known bug, ticket 412')
def test_known_bug():
    assert 1 == 2

@pytest.mark.xfail(reason='fixed last week, nobody removed the mark')
def test_already_fixed():
    assert 1 == 1

@pytest.mark.skip(reason='needs a database')
def test_skipped():
    assert False
