import sys

def clean_expression(exp):
    exp = exp.replace(' ', '').lower()
    return exp

def validation(exp):
    if len(exp) > 2:
        sys.exit("too many arguments")
    return exp[1]