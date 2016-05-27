#!/usr/bin/python
from scaner import Scaner
from parser import Parser
from codeGenerator import CodeGenerator
import sys

for line in sys.stdin:
	expression = str(line)
	break
print("Expression: " + expression)

scaner = Scaner()
parser = Parser()
codeGen = CodeGenerator()

tokens = scaner.scan(expression)
tree = parser.constructTree(tokens)
commands = codeGen.createCommands(tree)

cl = ""
for item in commands:
	print(item)
	cl = cl + item + ";"

sys.stdout.write(cl)
