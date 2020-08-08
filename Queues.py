#!/usr/bin/python

class Queues:
	def __init__(self):
		# initialise an empty queue with primitive collection list
		self.items = []

	def enqueue(self, item):
		# add the item to the rear
		# this implementation assumes that rear is at position 0
		# in the list. This allows us to use the insert function 
		# on lists to add new elements to the rear of the queue
		return self.items.insert(0, item)

	def dequeue(self):
		# remove an item from the front of the queue
		return self.items.pop()

	def size(self):
		# return the size of the queue
		return len(self.items)

	def isEmpty(self):
		# return True if queue is empty else return False
		return self.items == []

	def peek(self):
		# show the last item in the queue
		return self.items[len(self.items)-1]


#main
q = Queues()
q.enqueue("shilpa")
q.enqueue("jatheen")
q.enqueue("ishaan")
q.enqueue("nishka")
#for i in q.items:
#	print i
#print q.dequeue()
#print q.peek() # does not remove the item from the list. It just displays the item
#print q.peek()

"""
Problem : Hot Potato
"""
def hotPotato(nameList, num):
	que = Queues()
	for name in nameList:
		que.enqueue(name)

	#for name in que.items:
	#	print name

	while que.size() > 1:
		for n in range(num):
			que.enqueue(que.dequeue())
			print que.peek()

		
		que.dequeue()

	#print que.peek()
	return que.dequeue()

#main
nameList = ["shilpa", "jatheen", "ishaan", "nishak", "ramani", "rahul"]
last = hotPotato(nameList, 7)
print last

