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
            #For all the input tokens [S1] read the next token [S2]
        for token in tokens:
            if self.isOperator(token):
                    # If token is an operator (x) [S3]
                while len(stack) != 0 and self.isOperator(stack[-1]):
                        # [S4]
                    if (self.isAssociative(token, LEFT_ASSOC)
                        and self.cmpPrecedence(token, stack[-1]) <= 0) or (self.isAssociative(token, RIGHT_ASSOC)
                        and self.cmpPrecedence(token, stack[-1]) < 0):
                            # [S5] [S6]
                        out.append(stack.pop())
                        continue
                    break
                    # [S7]
                stack.append(token)
            elif token == '(':
                stack.append(token) # [S8]
            elif token == ')':
                    # [S9]
                while len(stack) != 0 and stack[-1] != '(':
                    out.append(stack.pop()) # [S10]
                stack.pop() # [S11]
            else:
                out.append(token) # [S12]
        while len(stack) != 0:
                # [S13]
            out.append(stack.pop())
        return out
