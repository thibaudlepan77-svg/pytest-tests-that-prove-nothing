def total(items, discount=0):
    s = sum(i['price'] * i['qty'] for i in items)
    return round(s * (1 - discount), 2)
