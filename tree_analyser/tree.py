
class PropositionalFormulaTree:
    class Element:
        def __init__(self, value):
            self.form = value # string value of element 
            self.left = None
            self.right = None
            self.value = None # boolean value of element


    def __init__(self, postfix):
        self.root = self.Element(postfix.pop())
        self.root.right = self.Element(postfix.pop())
        if self.isOperator(self.root.right.form):  self.setTree(self.root.right, postfix)
        self.root.left = self.Element(postfix.pop())
        if self.isOperator(self.root.left.form):  self.setTree(self.root.left, postfix)


    def isOperator(self, op):
        return op in ("or", "and", "not")


    def setTree(self, element, postfix):
        if element.form == "not":
            element.right = self.Element(postfix.pop())
            if self.isOperator(element.right.form): self.setTree(element.right, postfix)
        else:
            element.right = self.Element(postfix.pop())
            if (self.isOperator(element.right.form)): self.setTree(element.right, postfix)
            element.left = self.Element(postfix.pop())
            if (self.isOperator(element.left.form)): self.setTree(element.left, postfix)


    def show(self):
        self.showTree(self.root)


    def showTree(self, element):
        print(element.form)
        if element.left != None: self.showTree(element.left)
        if element.right != None: self.showTree(element.right)

    # test
    '''
    def showTree2(self, element):
        if element is not None:
            print(element.form)
            self.showTree2(element.left)
            self.showTree2(element.right)
    '''
