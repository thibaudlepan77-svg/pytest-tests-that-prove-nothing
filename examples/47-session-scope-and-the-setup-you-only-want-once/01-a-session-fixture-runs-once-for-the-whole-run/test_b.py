def test_two(rows):
    rows['rows'] += 1
    assert rows['rows'] == 1001
