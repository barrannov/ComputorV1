from reducion import *
from validation import *
from solving import *
from utils import *

# expression = validation(sys.argv)

# try:

a = ['-6 * x^2 - 5 * x^1 - 1 * x^0=0', #-0.5; -0.3
     "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0",

     ]


def begin_solving(exp):
    solution = {}

    solution['equation'] = exp
    expression = clean_expression(exp)

    expression = reduce(expression)

    solution['reduced_form'] = get_reduced_expression(expression)
    solution['solutions'] = []
    print('Reduced form: ' + solution['reduced_form'])

    solution['polynomial_degree'] = get_polynomial_degree(expression['first'])
    power = solution['polynomial_degree']
    print('Polynomial degree: ' + str(power))
    if power > 2:
        solution['message'] = "The polynomial degree is stricly greater than 2, I can't solve."
        print(solution['message'])
    elif power == 0:
        print('The solution is: ' + str(int(expression['first'][0]['number'])))
    else:
        solution.update(solve(expression))
        print(solution['message'])
        for s in solution['solutions']:
            print(s)

    return solution

# begin_solving(a[2])

# except Exception:
#     print('Invalid expression')
#
#
