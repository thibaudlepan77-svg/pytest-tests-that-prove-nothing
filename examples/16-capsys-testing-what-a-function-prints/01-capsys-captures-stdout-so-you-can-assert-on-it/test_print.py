def greet(name):
    print('Hello, ' + name)

def test_greet(capsys):
    greet('Ada')
    out, err = capsys.readouterr()
    assert out == 'Hello, Ada\n'
    assert err == ''
