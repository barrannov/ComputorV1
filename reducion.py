def change_sign(values):
    for d in values:
        d['sign'] = '-' if d['sign'] == '+' else '+'

    return values

def reduce(expression):

    parts = {}
    parts['first'] = expression.split('=')[0]
    parts['second'] = expression.split('=')[0]