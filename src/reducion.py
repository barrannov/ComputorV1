from utils import *

def change_sign_all_signs(values):
    for d in values:
        d['sign'] = '-' if d['sign'] == '+' else '+'

    return values


def find_next_term(exp):
    res = dict()

    res['sign'] = '-' if '-' in exp else '+'
    res['number'] = int(exp[:exp.index('*')])
    res['power'] = int(exp[exp.index('^') + 1:])

    return res


def to_terms(exp, parts, part_str="first"):
    """ split our equations int separate terms:

         5 * X^0 + 4 * X^1 = 4 * X^0 ->
         {'first':[
            {'number': 5, 'power':0, 'sign':'+'},
            {'number': 4, 'power':1, 'sign':'+'}]
        'second':[
            {'number': 4, 'power':0, 'sign':'+'}]
         }

    """

    res = {}

    if exp[0] == '-':
        res['sign'] = '-'
        exp = exp[1:]

    elif exp[0] == '+':
        res['sign'] = ''
        exp = exp[1:]
    else:
        res['sign'] = ''

    res['number'] = float(exp[:exp.index('*')])
    exp = exp[exp.index('*'):]
    res['power'] = int(exp[exp.index('^') + 1: exp.index('^') + 2])
    exp = exp[exp.index('^')+2:]

    parts[part_str].append(res)

    if exp:
        if exp[0] == '=':
            part_str = "second"
            exp = exp[1:]
        if len(exp) > 1:
            to_terms(exp, parts, part_str)

    return parts


def to_shorter(exp):
    """ simplifies everything what is after equals sign"""

    added = []

    for term_second in exp['second']:
        for term_first in exp['first']:
            if term_first['power'] == term_second['power']:
                term_second['sign'] = '' if term_second['sign'] == '-' else '-'
                term_first['number'] = eval(str(term_first['number']) + '+' + term_second['sign'] + str(term_second['number']))
                added.append(term_second)
                break

    for term in exp['second']:
        if term not in added:
            term['sign'] = change_sign(term['sign'])
            exp['first'].append(term)

    return exp['first']


def reduce(expression):
    """ simplifies our equation

        5 * X^0 + 4 * X^1 = 4 * X^0 -> 1 * X^0 + 4 * X^1 = 0

        and send all parts of it back
    """

    parts = dict()

    # split our equation into two parts by '='
    parts['first'] = []
    parts['second'] = []

    parts = to_terms(expression, parts)
    exp = to_shorter(parts)
    return exp
