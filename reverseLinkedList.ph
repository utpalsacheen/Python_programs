# Given a linked list, write a function to reverse every k nodes (where k is an input to the function).


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next

    def reverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        # reverse first k nodes of the linked list
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

         # next is now a pointer to (k+1)th node
         # recuresively call for the list starting from current
         # and make rest of the list as next of first node
        if next is not None:
            head.next = self.reverse(next, k)

        return prev  


llist = LinkedList()
llist.push('a')
llist.push('b')
llist.push('c')
llist.push('d')
llist.push('e')

llist.printList()
print '\n'
llist.head = llist.reverse(llist.head, 3)
llist.printList()
