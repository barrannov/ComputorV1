from copy import deepcopy

from src.utils import *

"""All functions for solving equation"""


def clean_term_zero(terms):
    """ removes all zero terms, as we don't need them for solving
        zero term is term with zero number, for example {'number':0, 'sign':'', power:'2'} == 0 * X^2
    """

    for term in terms:
        if term['number'] == 0:
            terms.remove(term)
    return terms


def remove_zero(number):
    """removes trailing zero 1.0 -> 1, 1.12 -> 1.12"""

    if number == int(number):
        return int(number)
    else:
        return number


def count_root(value):
    """ counts squad root for any number, up to 0.000001 precision
        count_root(324) == 17.999999
    """

    if value == 0:
        return 0
    dot = 0.000001

    precision = 1.0
    res_root = 0.0

    while precision > dot:
        while res_root * res_root < value:
            res_root += precision
        res_root -= precision
        precision /= 10

    return round(res_root, 6)


def find_roots_for_squad_exp(disc, sign='+'):
    """ finds rots of equations for solving squad equations
        x = (-b sign count_root(D)) / (2a)

        sign could be '+' or '-' as well
        count_root - function for counting squad root

    """

    two_a = eval(disc['a']['sign'] + str(float(disc['a']['number']))) * 2
    disc['b']['sign'] = change_sign(disc['b']['sign'])
    root_disc = count_root(disc['disc'])
    exp_up = '(' + disc['b']['sign'] + str(disc['b']['number']) + sign + str(float(root_disc)) + ')'
    res_up = eval(exp_up)

    res = res_up / two_a
    return remove_zero(round(res, 6))


def solve_simple(exp):
    if exp[0]['power'] == 1:
        a = exp[0]
        b = exp[1]

    else:
        b = exp[0]
        a = exp[1]
    b['sign'] = change_sign(b['sign'])
    exp = b['sign'] + str(b['number']) + '/' + str(a['number'])
    return eval(exp)


def find_discriminant(exp):

    # D = b2 - 4ac

    a = 0
    b = 0
    c = 0
    for term in exp:
        if term['power'] == 0:
            c = term
        elif term['power'] == 1:
            b = term
        elif term['power'] == 2:
            a = term
    # b2 counting
    to_solve_square = eval(b['sign'] + str(float(b['number'])) + '*' + b['sign'] + str(float(b['number'])))

    # b2 - 4ac counting
    sol = str(to_solve_square) + '-4' + '*' + a['sign'] + str(float(a['number'])) + '*' + c['sign'] + str(float(c['number']))
    disc = eval(sol)
    return {'a': a, 'b': b, 'c': c, 'disc': disc}


def solve_squad(exp):
    disc = find_discriminant(exp)

    # if discriminant > 0 there are two solutions should be
    if disc['disc'] > 0:
        sol2 = find_roots_for_squad_exp(deepcopy(disc))
        sol1 = find_roots_for_squad_exp(deepcopy(disc), '-')
        return {'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
                'solutions': [sol1, sol2]}

    # if discriminant == 0 there is one solution should be
    elif disc['disc'] == 0:
        sol1 = find_roots_for_squad_exp(disc)
        return {'message': MESSAGE_DISCRIMINANT_EQUALS_ZERO,
                'solutions': [sol1]}

    # if discriminant < 0 there are no solutions should be
    else:
        return {'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG,
                'solutions': []}


def solve(exp):
    """solving polynomial equations"""

    exp = clean_term_zero(exp)

    if len(exp) == 2:
        # 1 * X^0 + 2 * X^1 = 0
        return {'message': THE_SOLUTION_IS,
                'solutions': [solve_simple(exp)]}
    elif len(exp) == 3:
        # 1 * X^0 + 2 * X^1 - 3 * X^2= 0
        return solve_squad(exp)
