from infix import InfixToPostfix 
from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation

form = "( a or b ) and ( a or b )"
A = InfixToPostfix(form.split())
print(A.postfix)
B = PropositionalFormulaTree(A.postfix)
# B.show()
tree_valuation(B)
