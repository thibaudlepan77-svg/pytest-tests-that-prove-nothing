class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError('amount must be positive')
    if amount > balance:
        raise InsufficientFunds('balance is ' + str(balance))
    return round(balance - amount, 2)
