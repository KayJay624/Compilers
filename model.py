#Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

#Supported operators
OPERATORS = {
	'+' : (0, LEFT_ASSOC),
	'-' : (0, LEFT_ASSOC),
	'*' : (5, LEFT_ASSOC),
	'/' : (5, LEFT_ASSOC),
	'%' : (5, LEFT_ASSOC),
	'^' : (10, RIGHT_ASSOC),
	'sin' : (7, LEFT_ASSOC),
	'cos' : (7,LEFT_ASSOC),
	'tan' : (7,LEFT_ASSOC)
}
	
#Test if a certain token is operator
def isOperator(token):
    return token in OPERATORS.keys()
	
#Test the associativity type of a certain token
def isAssociative(token, assoc):
	if not isOperator(token):
		raise ValueError('Invalid token: %s' % token)
	return OPERATORS[token][1] == assoc
	
#Compare the precedence of two tokens
def cmpPrecedence(token1, token2):
	if not isOperator(token1) or not isOperator(token2):
		raise ValueError('Invalid tokens: %s %s' % (token1, token2))
	return OPERATORS[token1][0] - OPERATORS[token2][0]
