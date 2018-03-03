from validation import validation
import sys
from reducion import *
from validation import *
from solving import *
from utils import *

# expression = validation(sys.argv)

# try:
expression = clean_expression('3 * X^0 + 1 * X^1 = 0 * X^0 - 1 * X^1 - 3 * X^2')

expression = reduce(expression)
print('Reduced form: ' + get_reduced_expression(expression))

power = get_polynomial_degree(expression['first'])
print('Polynomial degree: ' + str(power))
if power > 2:
    print("The polynomial degree is stricly greater than 2, I can't solve.")
elif power == 0:
    print('The solution is: ' + str(int(expression['first'][0]['number'])))
else:
    solution = solve(expression)
    print(solution['message'])
    for s in solution['res']:
        print(s)

# except Exception:
#     print('Invalid expression')
#
#
