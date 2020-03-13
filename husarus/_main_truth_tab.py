from tree import PropositionalFormulaTree
from analysing_tools import tree_valuation
from smart_split import smart_split
from converter import convert



def truth_table(items):
    tree = PropositionalFormulaTree(items)
    table, variables = tree_valuation(tree)
    return table, variables


def preliminary_processing(form):
    return convert(smart_split(form))



if __name__ == "__main__":
    form = input("enter form> ")
    print(truth_table(preliminary_processing(form))[0])
