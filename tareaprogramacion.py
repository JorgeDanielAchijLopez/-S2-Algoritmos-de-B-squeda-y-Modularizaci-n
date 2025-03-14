class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, element):
        self.items.append(element)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = Stack()
    output = []
    
    tokens = expression.split()
    
    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ' '.join(output)

# Ejemplo de uso
expresion_valida = "( 3 + 2 ) * ( 8 / 4 )"
expresion_invalida = "(( 3 + 2 ) * ( 8 / 4 )"
print(is_balanced(expresion_valida))  # True
print(is_balanced(expresion_invalida))  # False

expresion_infix = "3 + 5 * ( 2 - 8 )"
print(infix_to_postfix(expresion_infix))  # 3 5 2 8 - * +
