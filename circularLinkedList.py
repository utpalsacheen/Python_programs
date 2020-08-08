"""
Problem : Circular Singly Linked List


"""

class Node():
	# constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLL():
	# constructor to create an empty circular linked list
	def __init__(self):
		self.head = None

	# function to insert a node at the begining of a circular linked list
	def push(self, data):
		new_node = Node(data)
		temp = self.head

		new_node.next = self.head

		# if linked list is not None then set the next of last node
		if self.head is not None:
			while temp.next is not self.head:
				temp = temp.next
			temp.next = new_node
		else:
			new_node.next = new_node # for the first node

		self.head = new_node

	# function to print nodes in a given circular linked list
	def printLL(self):
		temp = self.head
		if self.head is not None:
			while True:
				print "%d" %(temp.data)
				temp = temp.next
				if temp == self.head:
					break

	# check if the linked list is circular or not
	def isCircular(self):
		temp = self.head

		if self.head is None:
			return True

		if self.head is not None:
			while temp is not None and temp is not self.head:
				temp = temp.next

		return temp == self.head


# driver program to test above function
# initialize list as empty
cc = CircularLL()

# created linked list will be 11->2->56->12
cc.push(12)
cc.push(56)
cc.push(2)
cc.push(11)

cc.printLL()
circular = cc.isCircular()
print circular
