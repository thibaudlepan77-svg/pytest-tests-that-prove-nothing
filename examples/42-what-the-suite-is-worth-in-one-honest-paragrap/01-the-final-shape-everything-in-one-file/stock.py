class OutOfStock(Exception):
    pass

def take(stock, item, n):
    if n <= 0:
        raise ValueError('n must be positive')
    if stock.get(item, 0) < n:
        raise OutOfStock(item)
    stock[item] -= n
    return stock[item]
