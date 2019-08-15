from infix import InfixToPostfix
from tree import PropositionalFormulaTree
from tree import find_operator_alpha
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert


for i in range(2):
    # form = "(a or b) and (a or not c)" # if you are lazy when you have to again type new form
    form = input("enter form> ")
    B = PropositionalFormulaTree(convert(smart_split(form)))
    print(tree_valuation(B))
