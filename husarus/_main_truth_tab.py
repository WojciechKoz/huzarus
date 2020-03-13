from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert



def preliminary_processing(form):
    return convert(smart_split(form))

def truth_table(form):
    items = preliminary_processing(form)
    tree = PropositionalFormulaTree(items)
    table, variables = tree_valuation(tree)
    return table, variables


if __name__ == "__main__":
    form = input("enter form> ")
    print(truth_table(form)[0])
