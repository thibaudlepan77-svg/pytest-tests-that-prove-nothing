import pytest

def load(name):
    raise ValueError('unknown format: parquet')

def test_message():
    with pytest.raises(ValueError, match='unknown format'):
        load('x')

def test_wrong_message():
    with pytest.raises(ValueError, match='file not found'):
        load('x')
