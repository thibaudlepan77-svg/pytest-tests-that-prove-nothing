class LoadError(Exception):
    pass

def load(raw):
    try:
        return int(raw)
    except ValueError as e:
        raise LoadError('bad row') from e
