from utils import *

def remove_zero(number):
    if number == int(number):
        return int(number)
    else:
        return number


def count_root(value):
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

    return round(res_root, 12)


def find_roots_for_squad_exp(disc, sign):
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
    to_solve_square = eval(b['sign'] + str(float(b['number'])) + '*' + b['sign'] + str(float(b['number'])))
    sol = str(to_solve_square) + '-4' + '*' + a['sign'] + str(float(a['number'])) + '*' + c['sign'] + str(float(c['number']))
    disc = eval(sol)
    return {'a': a, 'b': b, 'c': c, 'disc': disc}


from copy import deepcopy


def solve_squad(exp):
    res = {'Message': '', 'solutions': []}
    disc = find_discriminant(exp['first'])
    if disc['disc'] > 0:
        sol2 = find_roots_for_squad_exp(deepcopy(disc), '+')
        sol1 = find_roots_for_squad_exp(deepcopy(disc), '-')
        return {'message': 'Discriminant is strictly positive, the two solutions are:',
                'solutions': [sol1, sol2]}

    elif disc['disc'] == 0:
        sol1 = find_roots_for_squad_exp(disc, '-')
        return {'message': 'Discriminant equals zero, the one solution is:',
                'solutions': [sol1]}

    else:
        return {'message': 'Discriminant is strictly negative, there are no solutions found.',
                'solutions': []}


def solve(exp):
    if len(exp["first"]) == 2:
        return {'message': 'The solution is: ',
                'solutions': [solve_simple(exp["first"])]}
    elif len(exp["first"]) == 3:
        return solve_squad(exp)
    print()
