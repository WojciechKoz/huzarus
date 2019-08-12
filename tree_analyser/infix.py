def precedence(op):
    """ returns precedence of operator """
    if op == "not":
        return 5
    elif op == "and":
        return 4
    elif op == "or":
        return 3
    elif op == "->":
        return 2
    elif op == "<->":
        return 1
    else:
        return 0
    ''' alternative form for that function :
    operator_values = {"not":5, "and":4, "or":3, "->":2, "<->":1}
    # first check default situation
    if op not in operators_values.keys():
        return 0
    return operators_values[op] # if op is an operator then returns his value
    '''


def is_operator(op):
    return op in ("or", "and", "not", "(", ")", "implies", "equals")


class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.stack = []
        self.postfix = []
        self.convert(infix)

    def convert(self, infix):
        """ converts infix into postfix"""
        for element in self.infix:
            if not is_operator(element):
                self.postfix.append(element)
            else:
                self.process_operator(element)
        while self.stack:
            self.postfix.append(self.stack.pop())
        return self.postfix

    def process_operator(self, op):
        """ processes operator and places it in the correct place in the postfix """
        if op == '(':
            self.stack.append(op)
        elif op == ')':
            while self.stack and self.stack[-1] != '(':
                self.postfix.append(self.stack.pop())
            self.stack.pop()
        elif not self.stack:
            self.stack.append(op)
        else:
            top_op = self.stack[-1]
            while precedence(top_op) >= precedence(op) and self.stack[-1] != '(':
                self.postfix.append(self.stack.pop())
                if not self.stack: break
                top_op = self.stack[-1]
            self.stack.append(op)
