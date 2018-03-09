MESSAGE_DISCRIMINANT_EQUALS_ZERO = "Discriminant equals zero, the one solution is:"
MESSAGE_DISCRIMINANT_IS_STRICTLY_POS = "Discriminant is strictly positive, the two solutions are:"
MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG = "Discriminant is strictly negative, there are two complex solutions found."
MESSAGE_GREATER_THAN_2_CANT_SOLVE = "The polynomial degree is stricly greater than 2, I can't solve."
THE_SOLUTION_IS = "The solution is: "
ALL_NUMBERS = "All the real numbers are solution."
NO_NUMBERS = "There are no possible solutions."
PRINT_RES = False


def get_polynomial_degree(terms):
    power = terms[0]['power']
    for term in terms:
        if power < term['power']:
            power = term['power']
    return power


def get_reduced_expression(exp):
    e = ''
    for term_first in exp:
        sign = ' + ' if term_first['sign'] == '' else ' - '
        e += sign
        e += str(float(term_first['number'])).split('.0')[0]
        e += ' * X^' + str(term_first['power'])

    return e[3:] + ' = 0'


def change_sign(sign):
    if sign == '':
        return '-'
    else:
        return ''

