#!/usr/bin/python

"""
Linked List Implementation
"""

class Node:
	# initialise the Node 
	def __init__(self, data):
		self.data = data
		self.next = None

	# get the data of the Node specified
	def getData(self):
		return self.data

	# get the next node 
	def getNext(self):
		return self.next

	# set the new data to the existing given node
	def setData(self, newData):
		self.data = newData

	# set the next reference with the newNext
	def setNext(self, newNext):
		self.next = newNext


class UnorderedList:
	# inistialize an unordered list
	def __init__(self):
		self.head = None

	# check if the list is empty
	def isEmpty(self):
		return self.head == None

	# add a new node to the list
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	# get the length of the linked list
	def length(self):
		count = 0
		current = self.head
		while current is not None:
			count += 1
			current = current.next
		return count

	# search for a given item in the linked list
	def search(self, item):
		current = self.head
		found = False
		while current is not None  and found == False:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	# remove an existing item from the list
	def remove(self, item):
		current = self.head
		prev = None
		found = False

		while not found:
			if current.getData() == item:
				found = True
			else:
				prev = current
				current = current.getNext()

		if prev == None:
			self.head = current.getNext()
		else:
			prev.setNext(current.getNext())

	# write function append, insert, index and pop for unordered linked list


# main
un = UnorderedList()
un.add(1)
un.add(2)
un.add(3)

assert un.isEmpty() == False, "UnorderedList is not empty"
assert un.length() == 3, "The length of the UnorderedList is 3"
assert un.search(2) == True, "Item 2 is in the linked list"
assert un.search(4) == False, "Item 4 is not in the linked list"
un.remove(3)
assert un.length() == 2, "The length of the linked list is 2"


"""
Ordered Linked List
"""
class OrderedLinkedList():
	def __init__(self):
		# inititalize the Ordered List
		self.head = None

	# check if the linked list is empty
	def isEmpty(self):
		return self.head == None

	# return the length of the linked list
	def length(self):
		current = self.head
		count = 0
		while current is not None:
			count += 1
			current = current.getNext()
		return count

	# remove an item from the linked list
	def remove(self, item):
		current = self.head
		prev = None
		found = False
		while not found:
			if current.getData() == item:
				found == True
			else:
				prev = current
				current = current.getNext()

		if prev == None:
			self.head = current.getNext()
		else:
			prev.setNext(current.getNext())

	# add an item to the ordered linked list
	def add(self, item):
		current = self.head
		newNode = Node(item)
		prev = None
		stop = False

		while current is not None and not stop:
			if current.getData() > newNode.getData():
				stop = True
			else:
				prev = current
				current = current.getNext()

		if prev == None:
			newNode.setNext(self.head)
			self.head = newNode
		else:
			newNode.setNext(current)
			prev.setNext(newNode)


	# search for the given item in the ordered linked list
	def search(self, item):
		found = False
		current = self.head

		while current is not None and found == False:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					return found
				else:
					current = current.getNext()

		return found

	# print the ordered linked list
	def printoo(self):
		current = self.head
		while current is not None:
			print(current.data)
			current = current.getNext()

	# reverse the ordered linked list
	def reverseLL(self):
		cur = self.head
		prv, nxt = None, None
		while cur:
			nxt = cur.getNext()
			cur.setNext(prv)
			prv = cur
			cur = nxt

		current = prv
		while current is not None:
			print current.data
			current = current.next

		self.head = prv
		return self.head



oo = OrderedLinkedList()
oo.add(3)
oo.add(5)
oo.add(6)
oo.add(2)
oo.add(4)
oo.add(1)
oo.printoo()
ro = oo.reverseLL()
ro.printoo()


