from model import *

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
			if not isOperator(item):
				node = Node(item)
				stack.append(node)
			else:
				node = Node(item)
				if item == 'sin' or item == 'cos' or item == 'tan':
					n1 = stack.pop()
					n2 = None
				#elif self.isStack(item, R):
				#	n1 = stack.pop()
				#	n2 = stack.pop()
				else:
					n1 = stack.pop()
					n2 = stack.pop()
										
				node.right = n1
				node.left = n2
				stack.append(node)
		node = stack.pop()
		return node
	
	#Transforms tokens to RPN
	def convertToRPN(self, tokens):
		out = []
		stack = []
		print tokens
		#For all the input tokens read the next token
		for token in tokens:
			# If token is an operator (x)
			if isOperator(token):
				# While there is an operator (y) at the top of the operators stack
				while len(stack) != 0 and isOperator(stack[-1]):
					# if (x) is left-associative and its precedence is less
					# or equal to that of (y) or (x) is right-associative
					# and its precedence is less than (y)
					if ((isAssociative(token, LEFT_ASSOC) and
						cmpPrecedence(token, stack[-1]) <= 0)
						or
						(isAssociative(token, RIGHT_ASSOC) and
						cmpPrecedence(token, stack[-1]) < 0)):
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
