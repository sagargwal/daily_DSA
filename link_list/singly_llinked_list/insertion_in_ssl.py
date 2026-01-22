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

    # for printing the linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result
    



    # for appending to the LL
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


    # for prepending to the LL
    def prepend(self, value):
        # prepend() adds a new node at the beginning of the linked list

        new_node = Node(value)  
        # Create a new node in heap memory
        # Time: O(1), Space: O(1)

        if self.head is None:
            # If the linked list is empty (no nodes present yet)
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # head now points to the new node (first node in list)
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # tail also points to the same node (only one node exists)
            # Time: O(1), Space: O(1)

        else:
            # If the linked list already has nodes
            # Time: O(1), Space: O(1)

            new_node.next = self.head  
            # Link new node to the old first node
            # new_node now points to current head
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # Move head reference to the new node
            # Now new node becomes the first node
            # Time: O(1), Space: O(1)

        self.length += 1  
        # Increase the size of the linked list
        # Time: O(1), Space: O(1)

    def insert(self, index, value):
        # insert() adds a new node at a given index in the linked list
        # It returns:
        #   True  → if insertion is successful
        #   False → if insertion fails (invalid index)

        new_node = Node(value)  
        # Create a new node in memory
        # Time: O(1), Space: O(1)

        if index < 0 or index > self.length:
            # If index is invalid (negative or greater than list length)
            # We CANNOT insert at this position

            # return False means:
            # - Stop the function immediately
            # - Tell the caller that insertion FAILED
            # - No changes will be made to the linked list
            # Time: O(1), Space: O(1)
            return False

        if self.head is None:
            # If linked list is empty and index is 0
            # This is the first node of the list

            self.head = new_node  
            # head now points to the new node
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # tail also points to the same node (only one node exists)
            # Time: O(1), Space: O(1)

        elif index == 0:
            # If inserting at the beginning of a non-empty list

            new_node.next = self.head  
            # New node points to the old first node
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # Move head to the new node (new node becomes first)
            # Time: O(1), Space: O(1)

        else:
            # If inserting in the middle or at the end (not index 0)

            temp_node = self.head  
            # Start traversal from head
            # Time: O(1), Space: O(1)

            for _ in range(index - 1):
                # Move to the node just BEFORE the insertion position
                # We must reach the correct place before linking
                # Loop runs (index-1) times
                # Time: O(n), Space: O(1)

                temp_node = temp_node.next  
                # Move one node forward using next reference
                # Time: O(1), Space: O(1)

            new_node.next = temp_node.next  
            # New node now points to the next node in the list
            # This preserves the remaining part of the linked list
            # Time: O(1), Space: O(1)

            temp_node.next = new_node  
            # Previous node now points to the new node
            # This inserts the new node into the chain
            # Time: O(1), Space: O(1)

            if new_node.next is None:
                # If new node was inserted at the very end
                # Then it becomes the new tail

                self.tail = new_node  
                # Update tail reference
                # Time: O(1), Space: O(1)

        self.length += 1  
        # Increase size of linked list because insertion succeeded
        # Time: O(1), Space: O(1)

        # return True means:
        # - Insertion was COMPLETED successfully
        # - All pointer updates worked correctly
        # - Inform the caller that operation SUCCEEDED
        # Time: O(1), Space: O(1)
        return True

    def traversal(self):
    # traversal() prints all values stored in the linked list
    # It visits each node one by one starting from head

        temp_node = self.head  
        # Start traversal from the first node of the linked list
        # temp_node holds a reference to the current node
        # Time: O(1), Space: O(1)

        while temp_node is not None:
            # Loop continues as long as the current node exists
            # This ensures we visit every node including the last one
            # The loop will run once for each node
            # Time: O(n), Space: O(1)

            print(temp_node.value)  
            # Print the value stored in the current node
            # Time: O(1), Space: O(1)

            temp_node = temp_node.next  
            # Move to the next node using the next reference
            # This follows the links between nodes
            # Time: O(1), Space: O(1)

    def search(self,value):
        current = self.head
        index = 0
        while current is not None: #this same as while current is not none 
            
            if current.value == value:
                return index
            current = current.next
            index+=1
        return -1

    

# Adding nodes to the linked list
new = Linkedlist()
new.append(103)
new.append(20)
new.append(20)
new.append(20)
# new.prepend(1)
# print(new.insert(3,17))
# print(new)
print(new.search(19990))
# Printing the value stored in the last node
# print(new.tail.value)
# in the end for whole the space and time complexity is O(1) and O(1)


