from validation import validation
import sys
from reducion import *
from validation import *
from solving import *
from get_funcs import *

# expression = validation(sys.argv)
expression = clean_expression("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^2 = 3 * X^0")
expression = reduce(expression)
print('Reduced form: ' + get_reduced_expression(expression))

power = get_polynomial_degree(expression['first'])
print('Polynomial degree: ' + str(power))
if power > 2:
    print("The polynomial degree is stricly greater than 2, I can't solve.")
else:
    expression = solve(expression)

