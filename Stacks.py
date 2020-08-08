#!/usr/bin/Python
import string

"""
Implementation of Stacks using List
Where the top is the begining of the list instead of the end.
using index position 0 explicitly while using pop and insert
to ensure the top is the begining.

Implementation using append and pop
 - this will perform push and pop in constant time O(1) no 
   matter how many items are on the stack

Implementation using insert(0) and pop(0)
 - this will perform insert(0) and pop(0) operations in O(N)
   for a stack of size N
"""
class Stacks:
	def __init__(self):
		# initialize a new stack using a primitive collection List
		self.items = []

    # return True if Stack is empty else return False
	def isEmpty(self):
		return self.items == []

	# push an item on a stack
	def push(self, item):
		# insert the item at index 0 - top of the stack
		#self.items.insert(0, item)
		self.items.append(item) # adds to the end of the list

	# remove an item from a stack
	def pop(self):
		# pop the top item from the list
		#return self.items.pop(0)
		return self.items.pop() # removes the item from the end of the list

	# show the item on the top of the stack
	def peek(self):
		#return self.items[0]
		return self.items[len(self.items)-1] # shows the item from the end of the list

	# size of the stack
	def size(self):
		return len(self.items)

#main
s = Stacks()
assert s.isEmpty() == True, "Stack should be empty!"
s.push("Shilpa")
s.push("Jatheen")
assert s.peek() == "Jatheen", "Top item on stack should be Jatheen"
s.push("Ishaan")
s.push("Nishka")
assert s.size() == 4, "Stack size should be 4!"
item = s.pop()
assert item == "Nishka", "Removed item should be Nishka"


def matches(open, close):
	opens = "({["
	closers = ")}]"

	return opens.index(open) == closers.index(close)

"""
Balanced Paranthesis problem: The general problem of balancing and nesting different
kinds of opening and cosing symbols properly
"""
def parChecker(string):
	s = Stacks()
	balanced = True
	index = 0

	while index < len(string) and balanced:
		symbol = string[index]
		if symbol in "{[(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced == False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False


# Cases for Balanced Paranthesis Problem
string = "{{({}{})}()}"
assert parChecker(string) == True, '{{({}{})}()} should havep balanced symbols'

string1 = "[[{{(())}}]]"
assert parChecker(string1) == True, "[[{{(())}}]] should have balanced symbols"

string2 = "((()]))"
assert parChecker(string2) == False, "((()])) should not have balanced symbols"


""" 
Problem : Converting decimal numbers to binary number
"""
def divideBy2(number):
	# to convert into any base
	# digits = "0123456789ABCDEF"

	s = Stacks()

	while number > 0:
		rem = number % 2
		s.push(rem)
		number = number // 2

	binary_string = ""
	while not s.isEmpty():
		binary_string = binary_string + str(s.pop())
		# binary_string = binary_string + digits[s.pop()]

	return binary_string


num = 233
binary_string = divideBy2(num)
print(binary_string)


"""
Problem : Infix-to-postfix conversion
example: ((A + B) * C)    --->  AB+C*
"""
def infixToPostfix(infixexpr):
	# create a dictionary to keep the presidenc of operators
	pres = {}
	pres['*'] = 3
	pres['/'] = 3
	pres['+'] = 2
	pres['-'] = 2
	pres['('] = 1

    # create a empty stack to save the operators
	opStack = Stacks()
	# create an empty list for the output
	postfixList = []

    # convert the infixexpr string to a list
	tokenList = infixexpr.split()

	import string

	for token in tokenList:
		if token in string.uppercase:
			postfixList.append(token)
		elif token == "(":
			opStack.push(token)
		elif token == ")":
			topToken = opStack.pop()
			while topToken != '(':
				postfixList.append(topToken)
				topToken = opStack.pop()
		else:
			while (not opStack.isEmpty()) and \
				(pres[opStack.peek()] >= pres[token]):
				postfixList.append(opStack.pop())
			opStack.push(token)

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())

	postfixexpr = "".join(postfixList)
	return postfixexpr



#main
infixexpr = "( ( A + B ) * C )"
postfixexpr = infixToPostfix(infixexpr)
assert postfixexpr == "AB+C*", "Infix ((A+B)*C) should be converted to Postfix: AB+C*"

infixexpr = "( ( A + B ) * ( C + D ) )"
postfixexpr = infixToPostfix(infixexpr)
assert postfixexpr == "AB+CD+*", "Infix ((A+B)*(C+D)) should be converted to Postfix: AB+CD+*"


"""
Problem: Postfix Evaluation
"""
def doMath(op, op1, op2):
	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2


def postfixEval(postfixexpr):
	# create an empty stack
	opStack = Stacks()

	# convert the postfix string to a lis
	tokenList = postfixexpr.split()

	for token in tokenList:
		if token in "0123456789":
			opStack.push(int(token))
		else:
			operand2 = opStack.pop()
			operand1 = opStack.pop()
			result = doMath(token, operand1, operand2)
			opStack.push(result)

	return opStack.pop()


#main
postfixexpr = "7 8 + 3 2 + /"
value = postfixEval(postfixexpr)
assert value == 3, "Postfix Evaluation should be 3"





