from infix import InfixToPostfix 
from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split


# form = "(a or b) and (a or not c)" # if you are lazy when you have to again type new form
form = input("enter form> ")
A = InfixToPostfix(smart_split(form))
B = PropositionalFormulaTree(A.postfix)
# print(form)
print(tree_valuation(B))
