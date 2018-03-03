def get_polynomial_degree(terms):
    power = terms[0]['power']
    for term in terms:
        if power < term['power']:
            power = term['power']
    return power


def get_reduced_expression(exp):
    e = ''
    for term_first in exp['first']:
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

