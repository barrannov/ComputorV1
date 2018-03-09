from src.reducion import *
from src.solving import *
from src.utils import *

from src.validation import *

PRINT_RES = True

""" 
    the main purpose of the program is to solve the polynomial equations

    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
"""


def print_res(res_to_print):
    print('Reduced form: ' + res_to_print['reduced_form'])
    print('Polynomial degree: ' + str(res_to_print['polynomial_degree']))
    print(res_to_print['message'])
    for s in res_to_print['solutions']:
        print(s)


def begin_solving(exp, res_print=False):
    # solution is a dictionary with results for printing in the end
    solution = dict()

    solution['equation'] = exp
    expression = clean_expression(exp)

    expression = reduce(expression)

    solution['reduced_form'] = get_reduced_expression(expression)
    solution['solutions'] = []

    solution['polynomial_degree'] = get_polynomial_degree(expression)
    power = solution['polynomial_degree']
    if power > 2:
        solution['message'] = "The polynomial degree is stricly greater than 2, I can't solve."
    elif power == 0:
        solution['message'] = THE_SOLUTION_IS
        solution['solutions'].append(remove_zero(expression[0]['number']))
    else:
        solution.update(solve(expression))

    if res_print:
        print_res(solution)

    return solution


try:
    res = begin_solving(validate(sys.argv), PRINT_RES)
except Exception:
    print('Invalid expression.')
