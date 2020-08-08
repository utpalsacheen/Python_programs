# Python program to compare two strings represented as
# linked lists

class Node:

    # constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.next = None


class LinkedList:

   # constructor to create a linkedlist
   def __init__(self):
       self.head = None

   # function to add the new_node
   def push(self, new_data):
       # add the new node at the begining of the linkedlist
       new_node = Node(new_data)
       new_node.next = self.head
       self.head = new_node

   def printList(self):
       temp = self.head
       while temp:
           print temp.data,
           temp = temp.next

def compareLists(l1, l2):
    while(l1 and l2 and l1.data == l2.data):
        l1 = l1.next
        l2 = l2.next

    if l1 and l2:
        return 1 if l1.data > l2.data else -1

    if l1 and not l2:
        return 1

    if l2 and not l1:
        return -1 

    return 0

# main
# create llist
llist = LinkedList() 
llist.push('g')
llist.push('h')
llist.push('i')
llist.push('k')
llist.printList()

# create 2nd llist1
llist1 = LinkedList() 
llist1.push('g')
llist1.push('h')
llist1.push('i')
llist1.push('k')
llist1.printList()

print compareLists(llist, llist1)
