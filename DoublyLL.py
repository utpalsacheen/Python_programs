"""
Problem: Doubly Linked List

"""

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyList():
	# constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None

	# Given a reference to the head of a list and an
	# integer, inserts a new node on the front of list
	def push(self, new_data):
		# allocate the new node
		new_node = Node(new_data)
		# make the next of the new node as head and 
		# prev as None (which is already None)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		# move the head to point to the new node
		self.head = new_node

	# Given a reference to the head of DLL and integer,
	# appends a new node at the end
	def append(self, new_data):
		# allocate the new node
		new_node = Node(new_data)
		# this new node is going to be the last node
		# so make next if it as None
		new_node.next = None
		# if LL is empty make it as new head
		if self.head is None:
			new_node.prev = None
			self.head = new_node
			return
		#else traverse until the last node
		last = self.head
		while last.next is not None:
			last = last.next

		last.next = new_node
		new_node.prev = last
		return

	# Given a node as prev_node, insert a new node after the given node
	def insertAfter(self, prev_node, new_data):
		# check if the given prev_node is None:
		if prev_node is None:
			print "The given prev node cannot be Null"
			return 

		# allocate the new node
		new_node = Node(new_data)

		# make the net of new node as next of prev node
		new_node.next = prev_node.next
		# make prev node as previous of new node
		prev_node.next = new_node
		# make prev node as previous of new node
		new_node.prev = prev_node
		# change previous of new nodes next node
		if new_node.next is not None:
			new_node.next.prev = new_node

	def remove(self, node_value):
		current = self.head
		while current is not None:
			if current.data == node_value:
				# if its not the first element
				if current.prev is not None:
					current.prev.next = current.next
					current.next.prev = current.prev
				else:
					self.head = current.next
					current.next.prev = None
			current = current.next

	def show(self):
		print "Show list data"
		current = self.head
		while current is not None:
			print current.prev.data if hasattr(current.prev, "data") else None,
			print current.data,
			print current.next.data if hasattr(current.next, "data") else None

			current = current.next
		print "*"*50

	# this function prints contents of linked list
	# starting from the given node
	def printList(self):
		print "traversal in forward direction\n"
		current = self.head
		while current is not None:
			print "-> %d" %(current.data),
			last = current
			current = current.next

		print "traversal in reverse direction\n"
		while last is not None:
			print "<- %d" %(last.data),
			last = last.prev



# main
d = DoublyList()
d.append(5)
d.append(7)
d.append(50)
d.append(30)
d.push(3)
d.insertAfter(d.head.next, 6)

#d.show()
d.printList()

d.remove(50)
d.remove(5)

#d.show()

