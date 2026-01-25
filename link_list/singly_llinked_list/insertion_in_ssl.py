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

    def search(self, value):
    # search() finds the position (index) of a given value in the linked list
    # It returns:
    #   index (0-based) → if value is found
    #   -1             → if value is not present in the list

        current = self.head  
        # Start searching from the first node (head)
        # current holds reference to the current node
        # Time: O(1), Space: O(1)

        index = 0  
        # Index counter to track the position of current node
        # First node has index 0
        # Time: O(1), Space: O(1)

        while current is not None:
            # Traverse through each node until the end of the list
            # Loop runs once for each node
            # Time: O(n), Space: O(1)

            if current.value == value:
                # Compare the value stored in current node
                # with the value we are searching for
                # If equal, value is found at this index
                # Time: O(1), Space: O(1)

                return index  
                # Stop searching and return the position of the value
                # This tells the caller EXACTLY where the value is located
                # Time: O(1), Space: O(1)

            current = current.next  
            # Move to the next node using the next reference
            # Time: O(1), Space: O(1)

            index += 1  
            # Move to the next index position
            # Time: O(1), Space: O(1)

        # If loop finishes, value was not found in any node
        return -1  
        # Returning -1 indicates that the value does NOT exist in the list
        # This is a standard convention in searching algorithms
        # Time: O(1), Space: O(1)

    def get(self, index):
    # get() returns the node present at a given index in the linked list
    # It returns:
    #   Node object → if index is valid
    #   None        → if index is invalid

        if index == -1:
            # Special case: if index is -1
            # We treat this as a shortcut to get the last node
            # Instead of traversing, we directly return tail
            # Time: O(1), Space: O(1)

            return self.tail

        if index < 0 or index > self.length:
            # If index is invalid (negative or greater than list length)
            # We cannot access a node at this position
            # Time: O(1), Space: O(1)

            return None

        temp_node = self.head  
        # Start traversal from the first node (head)
        # temp_node holds reference to the current node
        # Time: O(1), Space: O(1)

        for _ in range(index):
            # Move forward 'index' times to reach the desired node
            # Loop runs index times
            # Time: O(n), Space: O(1)

            temp_node = temp_node.next  
            # Move to the next node using next reference
            # Time: O(1), Space: O(1)

        return temp_node  
        # Return the node found at the given index
        # This allows the caller to access its value or next pointer
        # Time: O(1), Space: O(1)

    
    
    def set_value(self,index,value):  
        # temp_node = self.head
        # for _ in range(index):

        #     temp_node = temp_node.next 
        
        # temp_node.value = value
        
        # return None
 
        # set_value() updates the value of the node at a given index
        # It returns:
        #   True  → if update is successful
        #   False → if index is invalid (node not found)

        temp_node = self.get(index)  
        # Use the existing get() method to find the node at given index
        # This avoids rewriting traversal logic (code reuse)
        # Time: O(n), Space: O(1)
        # Note: get(index) itself may be O(1) or O(n) depending on index

        if temp_node:
            # If a valid node is returned (not None)
            # This means index is within range and node exists
            # Time: O(1), Space: O(1)

            temp_node.value = value  
            # Update the value stored in the node
            # This changes data but NOT the structure of the linked list
            # Time: O(1), Space: O(1)

            return True  
            # Return True to indicate update was successful
            # This tells the caller the operation SUCCEEDED
            # Time: O(1), Space: O(1)

        else:
            # If temp_node is None
            # This means get(index) failed → invalid index
            # Time: O(1), Space: O(1)

            return False  
            # Return False to indicate update FAILED
            # This tells the caller the operation did NOT succeed
            # Time: O(1), Space: O(1)

    def pop_first(self):
        # pop_first() removes and returns the first node of the linked list
        # It returns:
        #   removed node → if deletion is successful
        #   None         → if the list is empty

        temp_node = self.head  
        # Store current head node (may be None if list is empty)
        # Time: O(1), Space: O(1)

        if self.length == 0:
            # Edge case 1: If linked list is empty
            # Nothing to remove
            # Time: O(1), Space: O(1)

            return None

        if self.length == 1:
            # Edge case 2: If linked list has only one node
            # After removal, list should become empty
            # Time: O(1), Space: O(1)

            self.head = None  
            # Remove head reference
            # Time: O(1), Space: O(1)

            self.tail = None  
            # Remove tail reference (same as head in single-node list)
            # Time: O(1), Space: O(1)

        else:
            # Case 3: If linked list has more than one node
            # Time: O(1), Space: O(1)

            temp_node = self.head  
            # Store current head node so we can return it later
            # Time: O(1), Space: O(1)

            self.head = self.head.next  
            # Move head to the second node
            # This removes the first node from the list
            # Time: O(1), Space: O(1)

            temp_node.next = None  
            # Disconnect removed node from the list
            # Prevents accidental memory access
            # Time: O(1), Space: O(1)

        self.length -= 1  
        # Decrease size of linked list because one node is removed
        # Time: O(1), Space: O(1)

        return temp_node  
        # Return removed node to caller
        # Caller can access removed value if needed
        # Time: O(1), Space: O(1)


    def pop(self):
        # pop() removes and returns the last node of the linked list
        # It returns:
        #   removed node → if deletion is successful
        #   None         → if the list is empty

        pop_value = self.tail  
        # Store current tail node (the one we will remove)
        # This allows us to return it later
        # Time: O(1), Space: O(1)

        if self.length == 0:
            # Edge case 1: If linked list is empty
            # Nothing to remove
            # Time: O(1), Space: O(1)

            return None

        if self.length == 1:
            # Edge case 2: If linked list has only one node
            # After removal, list should become empty
            # Time: O(1), Space: O(1)

            self.head = None  
            # Remove head reference
            # Time: O(1), Space: O(1)

            self.tail = None  
            # Remove tail reference (same as head in single-node list)
            # Time: O(1), Space: O(1)

        else:
            # Case 3: If linked list has more than one node
            # We must find the SECOND-LAST node
            # Time: O(1), Space: O(1) for setup

            temp_node = self.head  
            # Start traversal from head to reach second-last node
            # Time: O(1), Space: O(1)

            while temp_node.next is not self.tail:
                # Move forward until we reach the node just before tail
                # Loop runs (n-1) times in worst case
                # Time: O(n), Space: O(1)

                temp_node = temp_node.next  
                # Move to next node using next reference
                # Time: O(1), Space: O(1)

            self.tail = temp_node  
            # Update tail to the second-last node
            # This removes the last node from the list
            # Time: O(1), Space: O(1)

            temp_node.next = None  
            # Disconnect the old tail node
            # Prevents accidental memory access
            # Time: O(1), Space: O(1)

        self.length -= 1  
        # Decrease size of linked list because one node is removed
        # Time: O(1), Space: O(1)

        return pop_value  
        # Return removed node to caller
        # Caller can access removed value if needed
        # Time: O(1), Space: O(1)



def remove(self, index):
    # remove() deletes the node at a given index in the linked list
    # It returns:
    #   removed node → if deletion is successful
    #   None         → if index is invalid or list is empty

    if index <-1 or index >= self.length:
        # If index is invalid (negative or beyond last index)
        # We cannot remove a node at this position
        # return None means:
        # - Stop function immediately
        # - Tell caller that deletion FAILED
        # Time: O(1), Space: O(1)

        return None

    if index == 0:
        # Edge case 1: Removing the first node
        # We reuse pop_first() to avoid rewriting logic
        # Time: O(1), Space: O(1)

        return self.pop_first()

    if index == self.length - 1 or index == -1:
        # Edge case 2: Removing the last node
        # We reuse pop() to avoid rewriting logic
        # Time: O(n), Space: O(1)

        return self.pop()

    # Case 3: Removing a node from the middle

    previous_node = self.get(index - 1)  
    # Get the node just BEFORE the one we want to remove
    # Time: O(n), Space: O(1)

    temp_node = previous_node.next  
    # Store the node to be removed
    # Time: O(1), Space: O(1)

    previous_node.next = temp_node.next  
    # Bypass the node to be removed
    # This reconnects the list and removes temp_node from chain
    # Time: O(1), Space: O(1)

    temp_node.next = None  
    # Disconnect removed node completely
    # Prevents accidental memory access
    # Time: O(1), Space: O(1)

    self.length -= 1  
    # Decrease size of linked list because one node is removed
    # Time: O(1), Space: O(1)

    return temp_node  
    # Return removed node to caller
    # Caller can access removed value if needed
    # Time: O(1), Space: O(1)





    

# Adding nodes to the linked list
new = Linkedlist()
new.append(103)
new.append(20)
new.append(20)
new.append(134)
print(new)
print(new.pop())
print(new)
# new.prepend(1)
# print(new.insert(3,17))
# print(new)
# print(new.search(19990))
# Printing the value stored in the last node
# print(new.tail.value)
# in the end for whole the space and time complexity is O(1) and O(1)


