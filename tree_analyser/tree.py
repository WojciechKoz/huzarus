# from infix import precedence # missing infix module


def precedence(op):
    operators = {"equals": 1, "implies": 2, "or": 3, "and": 4, "not": 5}
    if op not in operators.keys():
        return 0
    return operators[op]


def is_operator(op):
    return op in ("or", "and", "not", "implies", "equals")


def find_operator_alpha(formula):
    """ returns index of the most powerful operator """
    top_index = None
    brackets = 0
    i = 0
    while i < len(formula):
        print(i, len(formula))
        if formula[i] == "(":
            brackets += 1
            while brackets > 0:
                i += 1
                if formula[i] == "(":
                    brackets += 1
                elif formula[i] == ")":
                    brackets -= 1
        if is_operator(formula[i]):
            if top_index is None:
                top_index = i
            if precedence(formula[top_index]) == 2:
                if precedence(formula[top_index]) > precedence(formula[i]):
                    top_index = i
            else:
                if precedence(formula[top_index]) >= precedence(formula[i]):
                    top_index = i
        i += 1
    return top_index


class PropositionalFormulaTree:
    class Element:
        def __init__(self, value):
            self.form = value  # string value of element
            self.left = None
            self.right = None
            self.value = None  # boolean value of element
            self.describe = ""

    def __init__(self, formula):
        self.root = self.set_tree(formula)

    def set_tree(self, formula):
        # print(formula)
        if len(formula) is 1:
            return self.Element(formula[0])
        if formula[0] == "(" and formula[-1] == ")":
            return self.set_tree(formula[1:][:-1])
        alpha = find_operator_alpha(formula)
        current = self.Element(formula[alpha])
        if current.form != "not":
            current.left = self.set_tree(formula[:alpha])  # set subtree for left side of formula
            current.right = self.set_tree(formula[alpha + 1:])  # set subtree for right side of formula
            return current
        else:
            current.right = self.set_tree(formula[alpha + 1:])
            return current

    def show(self):
        self.show_tree(self.root)

    def show_tree(self, element):
        print(element.form)
        if element.left is not None:
            self.show_tree(element.left)
        if element.right is not None:
            self.show_tree(element.right)
