import unittest
from reducion import reduce

def get_reduced_expression_for_testing(exp):
    exp = exp.replace(' ', '')

    exp = reduce(exp)
    e = ''
    for term_first in exp['first']:
        sign = ' + ' if term_first['sign'] == '' else ' - '
        e += sign
        e += str(float(term_first['number'])).split('.0')[0]
        e += ' * X^' + str(term_first['power'])

    return e[3:] + ' = 0'


class ReduceTestCases(unittest.TestCase):
    def test_reducing(self):
        exps = [
            {'before' : '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0',
             'after' : '5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0'},
            {'before' : "5 * X^0 + 4 * X^1 = 4 * X^0",
             'after' : '1 * X^0 + 4 * X^1 = 0'},
            {'before' : '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0',
             'after' : '4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0'}
        ]
        for exp in exps:
            self.assertEqual(get_reduced_expression_for_testing(exp['before']), exp['after'])

if __name__ == '__main__':
    unittest.main()