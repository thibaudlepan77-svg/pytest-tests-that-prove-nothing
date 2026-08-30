def collect(value, bucket=[]):
    bucket.append(value)
    return bucket

def test_first():
    assert collect(1) == [1]

def test_second():
    assert collect(2) == [2]
