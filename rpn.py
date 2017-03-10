#!/usr/bin/env python

def add(arg1, arg2):
	return arg1 + arg2

def calculate(arg):
	stack = list()
	for operand in arg.split():
		if operand == '+':
			stack.append(stack.pop() + stack.pop())
		else:
			stack.append(float(operand))
def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()
