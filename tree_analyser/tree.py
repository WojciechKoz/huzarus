
class PropositionalFormulaTree:
    class Element:
        def __init__(self, value):
            self.form = value # string value of element 
            self.left = None
            self.right = None
            self.value = None # boolean value of element
            self.describe = ""


    def __init__(self, postfix):
        self.root = self.Element(postfix.pop())
        self.root.right = self.Element(postfix.pop())
        if self.is_operator(self.root.right.form):  self.set_tree(self.root.right, postfix)
        self.root.left = self.Element(postfix.pop())
        if self.is_operator(self.root.left.form):  self.set_tree(self.root.left, postfix)


    def is_operator(self, op):
        return op in ("or", "and", "not")


    def set_tree(self, element, postfix):
        if element.form == "not":
            element.right = self.Element(postfix.pop())
            if self.is_operator(element.right.form): self.set_tree(element.right, postfix)
        else:
            element.right = self.Element(postfix.pop())
            if (self.is_operator(element.right.form)): self.set_tree(element.right, postfix)
            element.left = self.Element(postfix.pop())
            if (self.is_operator(element.left.form)): self.set_tree(element.left, postfix)


    def show(self):
        self.show_tree(self.root)


    def show_tree(self, element):
        print(element.form)
        if element.left != None: self.show_tree(element.left)
        if element.right != None: self.show_tree(element.right)

