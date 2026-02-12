'''A doubly linked list is a linked list where each node stores data and two pointers: one to the next node and one to the previous node.

It differs from a singly linked list because singly lists have only a next pointer (one-directional traversal), while doubly lists allow traversal in both forward and backward directions.'''

class Node():
    def __init__(self,value):
        
        self.value = value
        self.next = None
        self.prev = None #as thier should be a prev reff
    
    def __str__(self):

        return str(self.value)

class doubly_ll():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        to_return = ""
        temp_node = self.head
        while temp_node:
            to_return += str(temp_node.value)
            if temp_node.next is not None:
                to_return += "<->"
            temp_node = temp_node.next
        return to_return

    def append(self,value):

        new_node =  Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1

    def prepend(self,value):

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1

    def traversal(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next

    def r_traversal(self):
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev

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
        # get() returns the node at a given index in a DOUBLY linked list
        # It returns:
        #   Node object → if index is valid
        #   None        → if index is invalid

        if index < 0 or index >= self.length:
            # Invalid index (negative or beyond last index)
            # Time: O(1), Space: O(1)
            return None

        # Decide traversal direction
        # If index is in the first half → start from head
        # If index is in the second half → start from tail

        if index < self.length // 2:
            # First half of list → traverse forward
            # Time: O(n/2) ≈ O(n), Space: O(1)

            temp_node = self.head  
            # Start from head
            # Time: O(1), Space: O(1)

            for _ in range(index):
                # Move forward 'index' times
                # Time: O(n), Space: O(1)
                temp_node = temp_node.next

        else:
            # Second half of list → traverse backward
            # Time: O(n/2) ≈ O(n), Space: O(1)

            temp_node = self.tail  
            # Start from tail
            # Time: O(1), Space: O(1)

            for _ in range(self.length - 1, index, -1):
                # Move backward until reaching index
                # Time: O(n), Space: O(1)
                temp_node = temp_node.prev

        return temp_node  
        # Return node at requested index
        # Time: O(1), Space: O(1)

    def set(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        # insert() adds a new node at a given index in a DOUBLY linked list
        # It returns:
        #   True  → if insertion is successful
        #   None  → if index is invalid

        if index < 0 or index > self.length:
            # Invalid index:
            # For insert, valid indices are 0 to length (inclusive)
            # Time: O(1), Space: O(1)
            return None

        if index == 0:
            # Insert at beginning
            # prepend() already handles pointer updates + length
            # Time: O(1), Space: O(1)
            return self.prepend(value)

        elif index == self.length:
            # Insert at end (append case)
            # append() already handles pointer updates + length
            # Time: O(1), Space: O(1)
            return self.append(value)

        else:
            # Insert in the middle of the list
            # Time: O(n), Space: O(1)

            new_node = Node(value)
            # Create new node
            # Time: O(1), Space: O(1)

            temp_node = self.head
            # Start traversal from head
            # Time: O(1), Space: O(1)

            for _ in range(index - 1):
                # Move to node just BEFORE insertion point
                # Loop runs (index - 1) times
                # Time: O(n), Space: O(1)
                temp_node = temp_node.next

            forward_node = temp_node.next
            # This is the node currently at 'index'
            # We will insert new_node between temp_node and forward_node
            # Time: O(1), Space: O(1)

            # Step 1: Connect new_node to surrounding nodes
            new_node.next = forward_node
            new_node.prev = temp_node

            # Step 2: Update surrounding nodes to point to new_node
            temp_node.next = new_node
            forward_node.prev = new_node

            # Now structure becomes:
            # temp_node <-> new_node <-> forward_node

            self.length += 1
            # Increase size of linked list
            # Time: O(1), Space: O(1)

            return True
            # Indicate successful insertion
            # Time: O(1), Space: O(1)

    def pop_first(self):
        # pop_first() removes the first node from a DOUBLY linked list
        # It returns:
        #   The removed node → if list is not empty
        #   None → if list is empty

        if self.head is None:
            # Case 1: Empty list
            # Nothing to remove
            # Time: O(1), Space: O(1)
            return None

        temp_node = self.head
        # Store current head (node to remove)
        # Time: O(1), Space: O(1)

        if self.length == 1:
            # Case 2: Only one node in list
            # After removal, list becomes empty
            self.head = None
            self.tail = None
            # Time: O(1), Space: O(1)

        else:
            # Case 3: More than one node

            self.head = temp_node.next
            # Move head pointer to next node
            # Time: O(1), Space: O(1)

            self.head.prev = None
            # Remove backward link to old head
            # Time: O(1), Space: O(1)

            temp_node.next = None
            # Detach removed node completely
            # Time: O(1), Space: O(1)

        self.length -= 1
        # Decrease list size
        # Time: O(1), Space: O(1)

        return temp_node
        # Return removed node
        # Time: O(1), Space: O(1)

    # Overall:
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def pop(self):
        if self.head is None:
            return None
        poped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:

            self.tail = self.tail.prev
            self.tail.next = None
            poped_node.prev = None
        self.length -= 1
        return poped_node
    
    def remove(self,index):
        current = self.head 
        for _ in range(index-1):
            current= current.next
        forward = current.next.next
        remove_node = current.next 
        remove_node.next = None
        remove_node.prev = None
        current.next = forward
        forward.prev = current
        




        

        





new = doubly_ll()

new.append(10)
new.append(20)
new.append(30)
new.append(90) 
# new.pop_fir
new.remove(2)
print(new.head)