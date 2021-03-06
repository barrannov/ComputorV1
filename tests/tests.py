import unittest

from ComputorV1 import *

from src.utils import *

PRINT_RES = False

class SolveTestCases(unittest.TestCase):
    squad_equations_no_reduce_needed = [
        {'equation': '9 * X^2 - 12 * X^1 + 4 * X^0 = 0',
         'polynomial_degree': 2,
         'reduced_form': '9 * X^2 - 12 * X^1 + 4 * X^0 = 0',
         'message': MESSAGE_DISCRIMINANT_EQUALS_ZERO,
         'solutions': [0.666667]},

        {'equation': "1 * X^2 - 6 *X^0 + 1*X^1=0",
         'polynomial_degree': 2,
         'reduced_form': "1 * X^2 - 6 * X^0 + 1 * X^1 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-3, 2]},

        {'equation': "2 * X^2 + 1*X^1 - 3*X^0=0",
         'polynomial_degree': 2,
         'reduced_form': "2 * X^2 + 1 * X^1 - 3 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-1.5, 1]},

        {'equation': "1 * X^2 + 3 * X^1 - 4 * X^0 =0",
         'polynomial_degree': 2,
         'reduced_form': "1 * X^2 + 3 * X^1 - 4 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_POS,
         'solutions': [-4, 1]},

        {'equation': "5 * x^2 + 3 * x^1 + 7*x^0 = 0",
         'polynomial_degree': 2,
         'reduced_form': "5 * X^2 + 3 * X^1 + 7 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG,
         'solutions': ["-0.3 - i * 1.144552", "-0.3 + i * 1.144552"]},

        {'equation': "3 * X^0 + 1 * X^1 = 0 * X^0 - 1*X^1-3*X^2",
         'polynomial_degree': 2,
         'reduced_form': "3 * X^0 + 2 * X^1 + 3 * X^2 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG,
         'solutions': ["-0.333333 - i * 0.942809", "-0.333333 + i * 0.942809"]},

        {'equation': "1 * X^2 - 2 * X^1 + 34 * X^0 = 0",
         'polynomial_degree': 2,
         'reduced_form': "1 * X^2 - 2 * X^1 + 34 * X^0 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG,
         'solutions': ["1 - i * 5.744562", "1 + i * 5.744562"]},

        {'equation': "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1",
         'polynomial_degree': 2,
         'reduced_form': "4 * X^0 + 3 * X^1 + 3 * X^2 = 0",
         'message': MESSAGE_DISCRIMINANT_IS_STRICTLY_NEG,
         'solutions': ["-0.5 - i * 1.040833", "-0.5 + i * 1.040833"]},
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

    simple_equations_reduce_needed = [
        {'equation': "5 * X^0 + 4 * X^1 + 1 * X^2= 1 * X^2",
         'polynomial_degree': 2,
         'reduced_form': "5 * X^0 + 4 * X^1 + 0 * X^2 = 0",
         'message': THE_SOLUTION_IS,
         'solutions': [-1.25]
         },

        {'equation': "5 * X^0 + 4 * X^1 = 4 * X^0",
         'polynomial_degree': 1,
         'reduced_form': "1 * X^0 + 4 * X^1 = 0",
         'message': THE_SOLUTION_IS,
         'solutions': [-0.25]
         },
        
        {'equation': "5.5 * X^0 = 4 * X^0 + 7.2 * X^1",
         'polynomial_degree': 1,
         'reduced_form': "1.5 * X^0 - 7.2 * X^1 = 0",
         'message': THE_SOLUTION_IS,
         'solutions': [0.208333]
         },
    ]

    very_simple_equations = [
        {'equation': "42 * X^0 = 42 * X^0",
         'polynomial_degree': 0,
         'reduced_form': "0 * X^0 = 0",
         'message': THE_SOLUTION_IS,
         'solutions': [ALL_NUMBERS]
         },

        {'equation': "42 * X^0 = 58 * X^0",
         'polynomial_degree': 0,
         'reduced_form': "-16 * X^0 = 0",
         'message': THE_SOLUTION_IS,
         'solutions': [NO_NUMBERS]
         },
    ]

    def test_solve_squad_equations_no_reduce(self):
        for exp in self.squad_equations_no_reduce_needed:
            self.assertEqual(begin_solving(exp['equation'], PRINT_RES), exp)

    def test_solve_squad_equations_reduce(self):
        for exp in self.squad_equations_reduce_needed:
            self.assertEqual(begin_solving(exp['equation'], PRINT_RES), exp)

    def test_simple_equations_reduce(self):
        for exp in self.simple_equations_reduce_needed:
            self.assertEqual(begin_solving(exp['equation'], PRINT_RES), exp)

    def test_very_simple_equations_reduce(self):
        for exp in self.very_simple_equations:
            self.assertEqual(begin_solving(exp['equation'], PRINT_RES), exp)

