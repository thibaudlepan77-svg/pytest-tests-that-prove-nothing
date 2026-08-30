import sys

def main():
    args = sys.argv[1:]
    if not args:
        return 'usage: cli NAME'
    return 'hello ' + args[0]
