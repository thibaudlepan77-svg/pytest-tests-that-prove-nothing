def price(amount, member):
    if member:
        amount = amount * 0.9
    return round(amount, 2)
