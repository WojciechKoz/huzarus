import unittest
from tree import PropositionalFormulaTree 
from smart_split import smart_split
from converter import convert
from analysing_tools import tree_valuation

def run_test(form, index=None):
    if index is None:
        index = form

    table = tree_valuation(PropositionalFormulaTree(convert(smart_split(form))))
    return to_list(table, index)


def to_list(table, index):
    return [item for item in table[index]]


class test_truth_table(unittest.TestCase):
    def test_output(self):
        self.assertEqual(run_test('a and b'), [False, False, False, True])

        self.assertEqual(run_test('a and b'), run_test('(a and b)', 'a and b'))

        self.assertEqual(run_test('a or b and a'), \
                run_test('a or (b and a)', 'a or b and a'))

        self.assertEqual(run_test('a implies b implies c'), \
                run_test('a implies (b implies c)', 'a implies b implies c'))

        self.assertEqual(run_test('a'), [False, True])

        self.assertEqual(run_test('not(a and b)', 'not a and b'), \
                run_test('not a or not b'))


    def test_values(self):
        self.assertRaises(ValueError, run_test, '')
        self.assertRaises(ValueError, run_test, 'and')
        self.assertRaises(ValueError, run_test, 'or')
        self.assertRaises(ValueError, run_test, '   ')
        self.assertRaises(ValueError, run_test, '123')
        self.assertRaises(ValueError, run_test, './.,')


    def test_types(self):
        self.assertRaises(ValueError, run_test, True)
        self.assertRaises(ValueError, run_test, [])
        self.assertRaises(ValueError, run_test, 123)
        self.assertRaises(ValueError, run_test, b'a and b') # bytes
