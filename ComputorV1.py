from validation import validation
import sys
from reducion import reduce
from validation import *

# expression = validation(sys.argv)
expression = clean_expression("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
expression = reduce(expression)
print('')
