'''In a singly linked list, nodes are stored in non-contiguous memory, so insertion requires updating pointers.

There are three ways to insert a new node:

Insert at the beginning

Allocate memory for the new node.

Set new_node.next to the current head.

Update head to point to the new node.

The old first node remains linked after the new node.

Insert in the middle (after a given node)

Traverse the list from the head to find the required node.

Allocate memory for the new node.

Set new_node.next to the next node of the current node.

Update the current node’s next to the new node.

Insert at the end

Traverse the list to reach the last node.

Allocate memory for the new node.

Set the last node’s next to the new node.

Update the tail to point to the new node.

In all cases, insertion works by changing references (links) between nodes, not by shifting memory.'''

from sll_nodesnLL import Node  
# Import Node class (no runtime cost in algorithm analysis)
# Time: O(1), Space: O(1)


class Linkedlist:
    # LinkedList class manages nodes (HAS-A relationship)
    # Time: O(1), Space: O(1)

    def __init__(self):
        # Constructor initializes an empty linked list
        self.head = None      # head points to first node | Time: O(1), Space: O(1)
        self.tail = None      # tail points to last node  | Time: O(1), Space: O(1)
        self.length = 0       # stores number of nodes    | Time: O(1), Space: O(1)


    def append(self, value):
        # append() adds a new node at the end of the linked list

        new_node = Node(value)  
        # Create a new node in heap memory
        # Time: O(1), Space: O(1)

        if self.head is None:
            # If list is empty (no nodes present)
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # head now points to first node
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # tail also points to the same node (only one node exists)
            # Time: O(1), Space: O(1)

        else:
            # If list already has at least one node
            # Time: O(1), Space: O(1)

            self.tail.next = new_node  
            # Link last node to the new node
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # Move tail reference to the new last node
            # Time: O(1), Space: O(1)

        self.length += 1  
        # Increment the size of linked list
        # Time: O(1), Space: O(1)
# Adding nodes to the linked list
new = Linkedlist()
new.append(103)
new.append(20)

# Printing the value stored in the last node
print(new.tail.value)
# in the end for whole the space and time complexity is O(1) and O(1)