import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from unittest import TestCase, main
from functions.calc_functions import *

class TestCalc(TestCase):
    @classmethod
    def setUp(self):
        # calc_expr's variables
        self.__values1 = ('2', 'add', '9', 'sub', '20', 'div', '2')
        self.__values2 = ('4.3', 'add', '9.2', 'add', '3.4',
                          'mult', '2.3', 'sub', '2.4')

        # change_operator's variables
        self.__context = {'add': '+', 'sub': '-', 'mult': '*', 'div': '/'}
        self.__values3 = ('1', 'add', '234', 'sub', '9')
        self.__values4 = ('9', 'mult', '231', 'add',
                          '12', 'div', '8', 'sub', '42')

    def test_calc_expr(self):
        self.assertEqual(calc_expr(self.__values1), 1)
        self.assertEqual(calc_expr(self.__values2), 18.92)

    def test_change_operators(self):
        self.assertEqual(change_operators(self.__values3, self.__context),
                         ['1', '+', '234', '-', '9'])
        self.assertEqual(change_operators(self.__values4, self.__context),
                         ['9', '*', '231', '+', '12', '/', '8', '-', '42'])


if __name__ == "__main__":
    main()
