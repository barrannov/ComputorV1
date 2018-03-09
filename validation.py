import sys


def clean_expression(exp):
    replace_chars = [' ', '"']

    for c in replace_chars:
        exp = exp.replace(c, '')
    return exp.lower()


def validate(exp):
    if len(exp) > 2:
        sys.exit("Too many arguments.")
    elif len(exp) < 2:
        sys.exit("Please, give an expression.")
    return exp[1]