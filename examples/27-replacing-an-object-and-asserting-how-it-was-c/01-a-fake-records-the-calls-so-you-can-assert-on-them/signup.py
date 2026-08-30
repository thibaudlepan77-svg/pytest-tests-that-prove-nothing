import mailer

def register(email):
    mailer.send(email, 'Welcome')
    return {'email': email}
