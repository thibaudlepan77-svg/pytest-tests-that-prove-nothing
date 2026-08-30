import signup

def test_sends_welcome(monkeypatch):
    calls = []
    monkeypatch.setattr(signup.mailer, 'send',
                        lambda to, subject: calls.append((to, subject)))
    signup.register('ada@example.com')
    assert calls == [('ada@example.com', 'Welcome')]
