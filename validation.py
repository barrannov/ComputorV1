import sys


def validation(argv):
    if len(argv) > 2:
        sys.exit("too many arguments")
    return argv[1]