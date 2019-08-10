from itertools import product
import pandas as pd


conjunctions = {    # you can change second element of each pair 
    "and": "and",   # it depends on input e.g. when you use ^ as 'and' operator
    "or" : "or",    # then it will be "and":"^"
    "imp": "->",
    "iff": "<->",
    "not": "not"
}

functions = {
    conjunctions["and"]: lambda a, b: a and b,
    conjunctions["or"] : lambda a, b: a or b,
    conjunctions["imp"]: lambda a, b: not a or b,
    conjunctions["iff"]: lambda a, b: a == b,  
    conjunctions["not"]: lambda _, a: not a # we ignore first argument
}

# checks if given element of tree is a leaf (has no children)
is_leaf = lambda elem: not (elem.left or elem.right)


def find_tree_leaves(current, leaves=[]):
    """ returns all leaves in given tree as a list """
    if current is not None:
        if is_leaf(current):
            leaves.append(current)
        else:
            find_tree_leaves(current.left, leaves)
            find_tree_leaves(current.right, leaves)
            return leaves


def clear_old_values(current):
    """ sets 'value' parameter for each elements to None """
    if current is not None:
        current.value = None
        clear_old_values(current.left)
        clear_old_values(current.right)


def add_nodes(current, table):
    if is_leaf(current): return None # leaves have already been included 

    if current.left is None:
        add_nodes(current.right, table)
        current.describe = describe(current).rstrip(" ")
        table[current.describe] = []
    elif is_leaf(current.left) and is_leaf(current.right):
        current.describe = describe(current).rstrip(" ")
        table[current.describe] = []
    else:
        add_nodes(current.left, table)
        add_nodes(current.right, table)
        current.describe = describe(current).rstrip(" ")
        table[current.describe] = []


def describe(element):
    if element is None:
        return "" 
    return describe(element.left) + element.form +" "+ describe(element.right)


def evaluate(current, table):
    """ sets a boolean value for each element in tree """
    if current is None: return None
    if current.form in conjunctions.values():
        elem_value = functions[current.form](evaluate(current.left, table), evaluate(current.right, table))
        table[current.describe].append(elem_value)
        current.value = elem_value # that's a bonus when you want to show all elems value
    return current.value


def tree_valuation(tree):
    """ main function for tree valuation """

    clear_old_values(tree.root)
    leaves = find_tree_leaves(tree.root)
    variables_names = {var.form for var in leaves}

    output = {var_name:[] for var_name in variables_names}
    add_nodes(tree.root, output)
    for variables_values in product([False, True], repeat=len(variables_names)):
        variables_relation = {key:value for key, value in zip(variables_names, variables_values)}

        # fill all leaves with given variable values
        for leaf in leaves:
            leaf.value = variables_relation[leaf.form]

        for name, value in variables_relation.items():
            output[name].append(value)
        evaluate(tree.root, output)
        # update_table(tree.root, output)

    return pd.DataFrame(output)

