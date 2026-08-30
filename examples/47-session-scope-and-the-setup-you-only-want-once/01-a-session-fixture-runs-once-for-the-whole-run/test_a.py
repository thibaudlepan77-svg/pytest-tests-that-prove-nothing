def test_one(rows):
    rows['rows'] += 1
    assert rows['rows'] == 1001
