# Given a linked list which is sorted, how will you insert in sorted way

# Create a Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):

        # special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # locate the node before the point of insertion
            current = self.head
            while(current.next is not None and
                 current.next.data < new_node.data):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    
    # function to insert a new node at the begining
    #def push(self, new_data):
    #    new_node = Node(new_data)
    #    new_node.next = self.head
    #    self.head = new_data

    # utility function to print the linkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next


# Create a new LinkedList
llist = LinkedList()
# Add a new node to the llist
new_node = Node(5) 
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)
print "Create Linked List"
llist.printList()

