""" Linked List and its operations """

""" Given a pointer/reference to the head of a singly linked list, reverse it and 
    return the pointer/reference to the head of reversed linked list """
""" Itereative solution: Runtime Complexity : Linear O(n) """
"""                    : Memory Complexity : Constant O(1) - no extra memory required """
def iterative_reverse(head):
	if head is None or head.next is None:
		return head

	cur = head.next
	rev = head
	rev.next = None
	while cur is not None:
		temp = cur
		cur = cur.next
		temp.next = rev
		rev = temp
		
	return rev

""" Recursive Solution: Runtime Complexity - Linear, O(n) """
"""                   : Memory Complexity - Linear, O(n) """
""" Note: One thing to remember is to mentione to the interviewer 
that recursive solution uses stack, OS allocates stack memory and 
this solution can run out of memory for really large linked lists """ 
""" CHECK THE RECURSIVE SOLUTION AGAIN """
def recursive_reverse(head):
	if head is None or head.next is None:
		return head

	reversed_list = recursive_reverse(head.next)

	head.next.next = head
	head.next = None

	return reversed_list


""" Remove duplicate nodes from linked list """
""" Iterative solution : Runtime Complexit - Linear O(n) """
"""                    : Memory Complexity - Linear O(n) - to store visited nodes in hashset """
def remove_duplicate_iterative(head):
	if head is None:
		return head

	dup = set()
	dup.add(head.val)

	cur = head
	while cur.next is not None:
		if cur.next.val in dup:
			cur.next = cur.next.next
		else:
		    dup.add(cur.next.val)
		    cur = cur.next

	return head


""" Given head of linked list and a key, delete node with this given key from the linked list"""
""" Iterative Solution : Runtime Complexity - Linear, O(n) """
"""                    : Memory Complexity - Constant, O(1) """
def delete_node(head, key):
	if head is None:
		return head
	elif head.val == key:
		return head.next

	cur = head
	while cur.next is not None:
		if cur.next.val == key:
			cur.next = cur.next.next
		else:
			cur = cur.next

	return head

	""" Book solution
	prev = None
	cur = head

	while cur != None:
		if cur.val == key:
			if cur == head:
				head = head.next
				cur = head
			else:
				prev.next = cur.next
				cur = cur.next
		else:
			prev = cur
			cur = cur.next

		# if key not found
		if cur == None:
			return head

		return head
	"""

""" Insertion Sort of a Linked List"""
""" Given head pointer of linked list, sort it in ascending order """
""" Maintain two lists i.e. sorted and unsorted. """
""" Runtime Complexity : Polynomial, O(n^2) """
""" Memory Complexity:  Linear, O(n) """
def sort_insert(sortedl, unsorted):
	if unsorted == None:
		return sortedl

	if (sortedl == None or unsorted.val <= sortedl.val):
		unsorted.next = sortedl
		return unsorted

	cur = sortedl
	while cur.next != None and cur.next.val < unsorted.val:
		cur = cur.next

	unsorted.next = cur.next
	cur.next = unsorted

	return sortedl


def insertion_sort(head):
	sortedl = None
	cur = head

	while cur is not None:
		temp = cur.next
		sortedl = sort_insert(sortedl, cur)
		cur = temp

	return sortedl





"""	if head is None:
		return None

	# make the first node the start of the sorted list
	sortl = head
	sortl.next = None
	head = head.next

	while head is not None:
		cur = head
		head = head.next

		if cur.val < sortl.val:
			# advance the node
			cur.next = sortl
			sortl = cur
		else:
			search = sortl
			while search.next is not None and cur.val > search.next.val:
				search = search.next
			# current goes after search
			cur.next = search.next
			search.next = cur

	return sortl """








class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def printll(self):
        head = self
        while head is not None:
            print(head.val)
            head = head.next


node1 = Node(29)
node2 = Node(23)
node3 = Node(82)
node4 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4
ll = node1
ll.printll()

print("Iterative reverse list")
ll1 = iterative_reverse(ll)
ll1.printll()

print("Recursive reverse list")
ll2 = recursive_reverse(ll1)
ll2.printll()

node5 = Node(28)
node6 = Node(15)
node4.next = node5
node5.next = node6


print("Remove duplicates from the linked list")
ll.printll()

print("Removing")
ll3 = remove_duplicate_iterative(ll)
ll3.printll()

print("Deleting node with value 14 from the linked list")
ll4 = delete_node(ll3, 10)
ll4.printll()

print("Instertion Sort")
ll.printll()
print("Sorting...")
ll5 = insertion_sort(ll)
ll5.printll()
