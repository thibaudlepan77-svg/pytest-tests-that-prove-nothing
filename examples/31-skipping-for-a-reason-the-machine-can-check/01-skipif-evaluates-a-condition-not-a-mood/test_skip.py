import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3, 8),
                    reason='needs Python 3.8 or later')
def test_modern():
    assert True

@pytest.mark.skipif(sys.version_info >= (3, 8),
                    reason='only for Python 3.7 and older')
def test_legacy():
    assert False
