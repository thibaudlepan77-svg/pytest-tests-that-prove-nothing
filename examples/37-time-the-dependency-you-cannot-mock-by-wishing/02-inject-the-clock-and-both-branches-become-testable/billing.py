from datetime import datetime

def greeting(now=None):
    h = (now or datetime.now()).hour
    return 'good morning' if h < 12 else 'good afternoon'
