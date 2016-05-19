#!/usr/bin/python
import sys
import math

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def execute():
    if command_list[0].split(" ")[0] == "put":
        stack.append(num(command_list[0].split(" ")[1]))
    elif command_list[0] == "add":
        compute("add")
    elif command_list[0] == "sub":
		compute("sub")
    elif command_list[0] == "mul":
        compute("mul")
    elif command_list[0] == "div":
        compute("div")
    elif command_list[0] == "mod":
        compute("mod")
    elif command_list[0] == "pow":
        compute("pow")
    elif command_list[0] == "sin":
        compute("sin")
    elif command_list[0] == "cos":
        compute("cos")
    elif command_list[0] == "end":
        return end()
    else:
        raise Warning("Invalid command: %s" % (command_list[0])) 
    
    command_list.pop(0)
    return execute()

def compute(oper):
    try:
        if (oper == "add"):
            n = stack.pop() + stack.pop()
        elif (oper == "sub"):
	    	n = stack.pop() - stack.pop()
        elif (oper == "mul"):
            n = stack.pop() * stack.pop()
        elif (oper == "div"):
            n = stack.pop() / stack.pop()
        elif (oper == "mod"):
            n = stack.pop() % stack.pop()
        elif (oper == "pow"):
            n = stack.pop() ** stack.pop()
        elif (oper == "sin"):
            n = math.sin(stack.pop())
        elif (oper == "cos"):
            n = math.cos(stack.pop())
        stack.append(n)
    except:
        raise Warning("Two first values on the stack are not numbers") 

def end():
    n = stack[-1]
    del stack[:]
    del command_list[:]
    return n

command_list = []
stack = []
for line in sys.stdin:
    command_list = line.split(";")[:-1]
   
print(execute())


            
