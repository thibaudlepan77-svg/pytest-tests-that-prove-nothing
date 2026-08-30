class LoadError(Exception):
    pass

def load(raw):
    try:
        return int(raw)
    except ValueError:
        raise LoadError('bad row')
