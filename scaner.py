import sys, traceback
from model import *

class myError(RuntimeError):
	args = ""	
	def __init__(self, arg):
	  	self.args = arg


class Scaner:
	tokens = []
	tmp = []
	
	def scan(self,string):
		string = string.replace(" ","")
		string = string.replace("\n","")
		try:		
			self.lexicalAnalysis(string)
			self.isCorrect(self.tokens)
		except myError, e:
			print e.args
  			sys.exit(1)
		return self.tokens
	
	def lexicalAnalysis(self, inputstring):
		i = 0		
		while i < len(inputstring):
						
			if inputstring[i].isdigit() or inputstring[i]==".":
				self.tmp.append(inputstring[i]) 
			
			elif inputstring[i] == "(" or inputstring[i] == ")":
				if len(self.tmp) > 0:
					self.tokens.append(''.join(self.tmp))
					del self.tmp[:]		
				self.tokens.append(inputstring[i])			
			
			elif isOperator(inputstring[i]):
				if len(self.tmp) > 0:				
					self.tokens.append(''.join(self.tmp))
					del self.tmp[:]
				self.tokens.append(inputstring[i])	
		
			elif isOperator(inputstring[i:(i+3)]):
				self.tokens.append(inputstring[i:(i+3)])
				i=i+2
			

			else:
				raise myError("Unrecognised symbol: %s" % inputstring[i])
				print inputstring[i]
			
			if (i == len(inputstring)-1) and (len(self.tmp) > 0) :
				self.tokens.append(''.join(self.tmp))
				del self.tmp[:]		
			
			i=i+1	
		return self.tokens

	def isCorrect(self, expression):
		for i in range(0, len(expression)):
			
			if expression[i] == "(" or expression[i] == ")" or expression[i] == "sin" or expression[i] == "cos" or expression[i] == "tan":
				continue			
				
			if isOperator(expression[i]):
				if i == 0:
					raise myError("An operator at the beginning: %s" % expression[i])

				try:
					if isOperator(expression[i+1]) and expression[i+1] != "sin" and expression[i+1] != "cos" and expression[i+1] != "tan":
						raise myError("Two or more consecutive operators: %s, %s" %(expression[i], expression[i+1]))					
				except IndexError:
					raise myError("An operator at the end: %s" % expression[i])						

				continue
			
			try:
				if float(expression[i]):
					try:
						if float(expression[i+1]):
							raise Warning("Two or more consecutive numbers")
					except (ValueError, IndexError) as e:
						pass
		
			except ValueError:
				raise myError("Unknown expression: %s" % (expression[i])) 

