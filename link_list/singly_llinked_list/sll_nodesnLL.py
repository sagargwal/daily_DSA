# We are creating a Node class
# A Node is the basic building block of a Linked List
class Node:
    
    # This function runs automatically when we create a new Node object
    # 'value' is the data we want to store inside the node
    def __init__(self, value):
        
        # Store the given value inside the node
        self.value = value
        
        # 'next' will store the address/reference of the next node
        # Since this node is alone right now, next is None
        self.next = None

    # This method simply returns the value stored in the node
    def show_value(self):
        return self.value


# Creating an object (instance) of Node class
# This node stores the value 10
# node_1 = Node(10)

# Calling the show_value method to get the stored value
# print(node_1.show_value())





'''Composition: A class HAS another class and uses it as a part (e.g., LinkedList has Nodes).

Inheritance: A class IS another class and reuses its behavior (e.g., a neural network is an nn.Module).'''
# LinkedList is NOT a Node
# LinkedList HAS nodes and manages them
# This is why we DO NOT inherit Node here but we do composition
class LinkedList:
    def __init__(self, value):
        # __init__ is a function
        # it runs only once when the LinkedList object is created
        
        # new_node is a LOCAL variable
        # it exists ONLY while __init__ is running
        # when __init__ ends, new_node (the name) disappears
        new_node = Node(value)
        
        # self.head is an ATTRIBUTE of the LinkedList object
        # anything stored using self. survives even after __init__ ends
        # this is why we store the node using self.head
        self.head = new_node
        
        # length belongs to the LinkedList object
        self.length = 1


# Creating a LinkedList object
# This calls the __init__ function of LinkedList
new_ll = LinkedList(17)

# Accessing the value of the first node in the linked list
# new_ll.head is the node object
# .value is the data stored inside that node
# print(new_ll.head.value)




# the time and space complexity of the ll with one node is o(n)

