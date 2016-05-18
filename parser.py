#Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

#Supported operators
OPERATORS = {
    '+' : (0, LEFT_ASSOC),
    '-' : (0, RIGHT_ASSOC),
    '*' : (5, LEFT_ASSOC),
    '/' : (5, RIGHT_ASSOC),
    '%' : (5, RIGHT_ASSOC),
    '^' : (10, RIGHT_ASSOC)
}
    
class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class Parser:
    def constructTree(self, tokens):
        stack = []
        rpn = self.convertToRPN(tokens) 
        for item in rpn:
            if not self.isOperator(item):
                node = Node(item)
                stack.append(node)
            else:
                node = Node(item)
                if self.isAssociative(item, LEFT_ASSOC):               
                    n1 = stack.pop()
                    n2 = stack.pop()
                else:
                    n2 = stack.pop()
                    n1 = stack.pop()
                
                node.right = n1
                node.left = n2
                stack.append(node)
        node = stack.pop()       
        return node

    #Test if a certain token is operator
    def isOperator(self, token):
        return token in OPERATORS.keys()

    #Test the associativity type of a certain token
    def isAssociative(self, token, assoc):
        if not self.isOperator(token):
            raise ValueError('Invalid token: %s' % token)
        return OPERATORS[token][1] == assoc

    #Compare the precedence of two tokens
    def cmpPrecedence(self, token1, token2):
        if not self.isOperator(token1) or not self.isOperator(token2):
            raise ValueError('Invalid tokens: %s %s' % (token1, token2))
        return OPERATORS[token1][0] - OPERATORS[token2][0]

    #Transforms tokens to RPN
    def convertToRPN(self, tokens):
        out = []
        stack = []
        #For all the input tokens read the next token
        for token in tokens:
            # If token is an operator (x)
            if self.isOperator(token):
                # While there is an operator (y) at the top of the operators stack
                while len(stack) != 0 and self.isOperator(stack[-1]):
                    # if (x) is left-associative and its precedence is less 
                    # or equal to that of (y) or (x) is right-associative
                    # and its precedence is less than (y)
                    if ((self.isAssociative(token, LEFT_ASSOC) and 
                        self.cmpPrecedence(token, stack[-1]) <= 0) 
                        or
                        (self.isAssociative(token, RIGHT_ASSOC) and 
                        self.cmpPrecedence(token, stack[-1]) < 0)):
                        # Pop (y) from the stack
                        # Add (y) output buffer
                        out.append(stack.pop())
                        continue
                    break
                # Push (x) on the stack
                stack.append(token)
            # Else If token is left parenthesis, then push it on the stack
            elif token == '(':
                stack.append(token)
            
            # Else If token is a right parenthesis
            elif token == ')':
                # Until the top token (from the stack) is left parenthesis
                while len(stack) != 0 and stack[-1] != '(':
                    # Pop from the stack to the output buffer
                    out.append(stack.pop())
                
                # Also pop the left parenthesis but dont include it in the output buffer
                stack.pop()
            # Else add token to output buffer
            else:
                out.append(token)

        # While there are still operator tokens in the stack, pop them to output
        while len(stack) != 0:
            out.append(stack.pop())

        return out
