
class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.stack = []
        self.postfix = []
        self.convert()


    def convert(self):
        for element in self.infix:
            if not self.is_operator(element):
                self.postfix.append(element)
            else: self.proccess_operator(element)
        while self.stack:
            self.postfix.append(self.stack.pop())
        return self.postfix


    def is_operator(self, op):
        return op in ("or", "and", "not", "(", ")", "->", "<->")


    def proccess_operator(self, op):
        if op == '(': self.stack.append(op)
        elif op == ')':
            while self.stack and self.stack[-1] != '(':
                self.postfix.append(self.stack.pop())
            self.stack.pop()
        elif not self.stack: self.stack.append(op)
        else:
            topOp = self.stack[-1]
            while (self.precedence(topOp) >= self.precedence(op) and self.stack[-1] != '('):
                self.postfix.append(self.stack.pop())
                if not self.stack: break
                topOp = self.stack[-1]
            self.stack.append(op)


    def precedence(self, op):
        if op == "not": return 5
        elif op == "and": return 4
        elif op == "or" : return 3
        elif op == "->" : return 2
        elif op == "<->" : return 1
        else: return 0


