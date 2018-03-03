import re

def change_sign(values):
    for d in values:
        d['sign'] = '-' if d['sign'] == '+' else '+'

    return values

def find_next_term(exp):
    res = {}

    res['sign'] = '-' if '-' in exp else '+'
    res['number'] = int(exp[:exp.index('*')])
    res['power'] = int(exp[exp.index('^') + 1:])

    return res

def to_terms(exp, parts, part_str="first"):
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
    added = []
    for term_second in exp['second']:
        term_second['sign'] = '' if term_second['sign'] == '-' else '-'
        for term_first in exp['first']:
            if term_first['power'] == term_second['power']:
                term_first['number'] = eval(str(term_first['number']) + '+' + term_second['sign'] + str(term_second['number']))
                added.append(term_second)

    for term in exp['second']:
        if term not in added:
            term['sign'] = change_sign(term['sign'])
            exp['first'].append(term)


    #TODO shorting inside of first part
        pass

    e = ''
    for term_first in exp['first']:
        sign = ' + ' if term_first['sign'] == '' else ' - '
        e += sign
        e += str(float(term_first['number']))
        e += ' * X^' + str(term_first['power'])

    return e + '= 0'
def reduce(expression):

    parts = {}
    parts['first'] = []
    parts['second'] = []

    parts = to_terms(expression, parts)
    exp = to_shorter(parts)
    return parts
