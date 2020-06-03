import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from functions.parser_functions import *
from unittest import TestCase, main

class TestParser(TestCase):
    def setUp(self):
        self.__commands = ('add', 'sub', 'mult', 'div')

        # check_command's and check_expr's variables
        self.__values1 = ['@', '^', '~', '#']
        self.__values2 = ['add', 'sadk', 'sodo', 'mmas', 'odko', 'sub', '@']
        self.__values3 = ['2', 'add', '92', 'sub', 'mult', '39', '1.2', 'div']

        # check_expr's variables
        self.__values4 = ['1', 'add', '1', 'add', '9', 'add']
        self.__values5 = ['3.4', 'add', '3.2', 'mult', '1.0']
        self.__values6 = ['2', 'add', '8', 'mult', '1934920132', 'div', '2']
        self.__values7 = ['2', 'add', '8', 'mult', '1934920132', 'div', '1']

        # get_flag's variables
        self.__MAX_SUBCOMMANDS = 1
        self.__flags = ('-f', '-even', '-odd')
        self.__values8 = ['-f', '-odd', '3.2', '1', '9']
        self.__values9 = ['-a', '3.2', '1', '9']
        self.__values10 = ['10', 'add', '9', 'div', '2']
        self.__values11 = ['-f', '2.3', 'add', '1.2', '-f', '3.2', 'add']
        self.__values12 = ['-even', '2', 'add', '8', 'sub', '2']

        # is_float's variables
        self.__values13 = ('hello-world', '3', '.43', '0.41.2', 'brow','9.32j', '34.3 a', '99.2O')
        self.__values14 = ('394.4', '294.2', '214.2', '93.4', '93949402934.1', '23823.1', '1.0000003')
    
    def test_check_commands(self):
        self.assertFalse(check_commands(self.__values1, self.__commands))
        self.assertFalse(check_commands(self.__values2, self.__commands))
        self.assertTrue(check_commands(self.__values3, self.__commands))

    def test_check_expr(self):
        self.assertFalse(check_expr(self.__values1, ''))
        self.assertFalse(check_expr(self.__values2, '-f'))
        self.assertFalse(check_expr(self.__values3, ''))
        self.assertFalse(check_expr(self.__values4, ''))
        self.assertFalse(check_expr(self.__values4, '-f'))
        self.assertTrue(check_expr(self.__values5, '-f'))
        self.assertTrue(check_expr(self.__values6, '-even'))
        self.assertFalse(check_expr(self.__values7, '-even'))
        self.assertTrue(check_expr(self.__values7, 'not exist'))

    def test_get_flags(self):
        self.assertEqual(get_flags(self.__values8, self.__flags, self.__MAX_SUBCOMMANDS), -1)
        self.assertIsNone(get_flags(self.__values9, self.__flags, self.__MAX_SUBCOMMANDS)[0])
        self.assertIsNone(get_flags(self.__values10, self.__flags, self.__MAX_SUBCOMMANDS)[0])
        self.assertEqual(get_flags(self.__values11, self.__flags, self.__MAX_SUBCOMMANDS), -1)
        self.assertGreaterEqual(len(get_flags(self.__values12, self.__flags, self.__MAX_SUBCOMMANDS)), 0)

    def test_is_float_number(self):
        for value in self.__values13:
            self.assertFalse(is_float_number(value))
        
        for value in self.__values14:
            self.assertTrue(is_float_number(value))
    
    def test_is_number(self):
        self.assertFalse(is_number('2.3', int))
        self.assertTrue(is_number('3', int))
        self.assertFalse(is_number('hello', int))
        self.assertFalse(is_number('3j', int))

if __name__ == "__main__":
    main()