from infix import InfixToPostfix 
from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split

form = "(a or b) and (a or not c)"
A = InfixToPostfix(smart_split(form))
B = PropositionalFormulaTree(A.postfix)
print(form)
tree_valuation(B)
