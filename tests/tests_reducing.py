import unittest
from ComputorV1 import begin_solving

MESSAGE_DISCRIMINANT_EQUALS_ZERO = "Discriminant equals zero, the one solution is:"
MESSAGE_DISCRIMINANT_IS_STRICTLY_POS = "Discriminant is strictly positive, the two solutions are:"
MESSAGE_GREATER_THAN_2_CANT_SOLVE = "The polynomial degree is stricly greater than 2, I can't solve."

import sys
sys.stdout.flush()

class SolveTestCases(unittest.TestCase):
    squad_equations_no_reduce_needed = [
        {'equation' : '9 * X^2 - 12 * X^1 + 4 * X^0 = 0',
         'polynomial_degree': 2,
         'reduced_form' : '9 * X^2 - 12 * X^1 + 4 * X^0 = 0',
         'message': MESSAGE_DISCRIMINANT_EQUALS_ZERO,
         'solutions': [0.666667]},

        {'equation' : "1 * X^2 - 6 *X^0 + 1*X^1=0",
         'polynomial_degree': 2,
         'reduced_form' : "1 * X^2 - 6 * X^0 + 1 * X^1 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-3, 2]},

        {'equation' : "2 * X^2 + 1*X^1 - 3*X^0=0",
         'polynomial_degree': 2,
         'reduced_form' : "2 * X^2 + 1 * X^1 - 3 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-1.5, 1]},

        {'equation' : "1 * X^2 + 3 * X^1 - 4 * X^0 =0",
         'polynomial_degree': 2,
         'reduced_form' : "1 * X^2 + 3 * X^1 - 4 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-4, 1]},
    ]

    squad_equations_reduce_needed = [
        {'equation': '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0',
         'polynomial_degree': 3,
         'reduced_form': '5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0',
         'message': MESSAGE_GREATER_THAN_2_CANT_SOLVE,
         'solutions': []
         },
        {'equation': "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
         'polynomial_degree': 2,
         'reduced_form': '4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0',
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [0.905239, -0.475131]
         }
    ]

    def test_solve_squad_equations_no_reduce(self):
        for exp in self.squad_equations_no_reduce_needed:
            self.assertEqual(begin_solving(exp['equation']), exp)

    def test_solve_squad_equations_reduce(self):
        for exp in self.squad_equations_reduce_needed:
            self.assertEqual(begin_solving(exp['equation']), exp)


    def test_no_solution_exists(self):
        pass

    def test_simple_equations(self):
        pass

