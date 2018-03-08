import sys

def clean_expression(exp):
    replace_chars = [' ', '"']

    for c in replace_chars:
        exp = exp.replace(c, '')
    return exp.lower()

def validation(exp):
    if len(exp) > 2:
        sys.exit("too many arguments")
    return exp[1]