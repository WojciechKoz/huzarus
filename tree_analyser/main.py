from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert


form = "(a or b) and (a or not c)" # if you are lazy when you have to again type new form
#form = input("enter form> ")
print(form)
B = PropositionalFormulaTree(convert(smart_split(form)))
table = tree_valuation(B)
print(table)

