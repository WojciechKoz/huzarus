from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert


form = input("enter form> ")
B = PropositionalFormulaTree(convert(smart_split(form)))
table = tree_valuation(B)
print(table)

