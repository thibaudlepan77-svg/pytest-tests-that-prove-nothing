from datetime import datetime

def greeting():
    h = datetime.now().hour
    return 'good morning' if h < 12 else 'good afternoon'
