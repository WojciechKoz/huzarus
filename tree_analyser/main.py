from infix import InfixToPostfix
from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert


for i in range(2):
    # form = "(a or b) and (a or not c)" # if you are lazy when you have to again type new form
    form = input("enter form> ")
    A = InfixToPostfix(convert(smart_split(form)))
    print(A.postfix)
    B = PropositionalFormulaTree(A.postfix)
    # print(form)
    print(tree_valuation(B))
