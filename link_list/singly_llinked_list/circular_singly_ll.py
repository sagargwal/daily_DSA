class Node:
    def __init__(self, value):
        # Node represents a single element in the linked list
        # It stores data and a reference to the next node

        self.value = value  
        # Store the data inside the node
        # Time: O(1), Space: O(1)

        self.next = None  
        # Initialize next pointer as None
        # This will later point to another node
        # Time: O(1), Space: O(1)
    def __str__(self):
        return str(self.value)

class CSLinked_List:
    def __init__(self):
        # CSLinked_List represents a Circular Singly Linked List
        # In a circular list, the last node points back to the first node

        # new_node = Node(value)  
        # Create a new node in heap memory
        # This will be the ONLY node initially
        # Time: O(1), Space: O(1)

        # new_node.next = new_node  
        # Make the node point to itself
        # This creates a CIRCLE:
        # head → node → node → node → ...
        # Time: O(1), Space: O(1)

        self.head =   None
        # Time: O(1), Space: O(1)

        self.tail = None  
        # tail also points to the same node
        # In circular list, tail.next should always point to head
        # Time: O(1), Space: O(1)

        self.length = 0 
        # Initialize list length as 1 (one node exists)
        # Time: O(1), Space: O(1)



    def append(self, value):
        # append() adds a new node at the END of the circular linked list
        # In a circular list:
        #   - tail.next must always point to head
        # This function maintains that rule

        new_node = Node(value)  
        # Create a new node in heap memory
        # This node will be added to the list
        # Time: O(1), Space: O(1)

        if self.length == 0:
            # Edge case 1: If the circular linked list is empty
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # head now points to the new node (first node in list)
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # tail also points to the same node
            # Time: O(1), Space: O(1)

            new_node.next = new_node  
            # New node points to itself to form a circle
            # head → node → node → node → ...
            # Time: O(1), Space: O(1)

        else:
            # Case 2: If the circular linked list already has nodes
            # Time: O(1), Space: O(1)

            self.tail.next = new_node  
            # Old tail now points to the new node
            # This inserts new node after the last node
            # Time: O(1), Space: O(1)

            new_node.next = self.head  
            # New node points back to head to maintain circular structure
            # Without this, the circle would break
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # Update tail to the new last node
            # Time: O(1), Space: O(1)

        self.length += 1  
        # Increase size of linked list because one node is added
        # Time: O(1), Space: O(1)

    def __str__(self):
    # __str__() converts the circular linked list into a readable string
    # This allows us to do: print(linked_list)
    # Example output: 10->20->30

        result = ""  
        # This string will store all node values in order
        # Time: O(1), Space: O(1)

        temp_node = self.head  
        # Start traversal from the first node (head)
        # temp_node holds reference to the current node
        # Time: O(1), Space: O(1)

        while temp_node is not None:
            # Loop to traverse the circular linked list
            # We CANNOT rely on temp_node becoming None
            # because in a circular list there is NO None at the end
            # Time: O(n), Space: O(1)

            result += str(temp_node.value)  
            # Add current node's value to result string
            # Time: O(1) per node (amortized), Space: O(1)

            temp_node = temp_node.next  
            # Move to the next node using next reference
            # Time: O(1), Space: O(1)

            if temp_node == self.head:
                # If we have come back to the head again
                # This means we have completed one full circle
                # So we must STOP to avoid infinite loop
                # Time: O(1), Space: O(1)

                break

            result += "->"  
            # Add arrow separator between node values
            # This makes output readable: 10->20->30
            # Time: O(1), Space: O(1)

        return result  
        # Return the final string representation of the list
        # Time: O(1), Space: O(1)


    def prepend(self, value):
        # prepend() adds a new node at the BEGINNING of the circular linked list
        # In a circular list:
        #   - tail.next must always point to head
        # This function maintains that rule while inserting at front

        new_node = Node(value)  
        # Create a new node in heap memory
        # This node will become the new head
        # Time: O(1), Space: O(1)

        if self.length == 0:
            # Edge case 1: If the circular linked list is empty
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # head now points to the new node (first node in list)
            # Time: O(1), Space: O(1)

            self.tail = new_node  
            # tail also points to the same node
            # Time: O(1), Space: O(1)

            new_node.next = new_node  
            # New node points to itself to form a circle
            # head → node → node → node → ...
            # Time: O(1), Space: O(1)

        else:
            # Case 2: If the circular linked list already has nodes
            # Time: O(1), Space: O(1)

            self.tail.next = new_node  
            # Old tail now points to the new node
            # This prepares the circle for new head insertion
            # Time: O(1), Space: O(1)

            new_node.next = self.head  
            # New node points to the old head
            # This keeps the rest of the list connected
            # Time: O(1), Space: O(1)

            self.head = new_node  
            # Move head reference to the new node
            # New node becomes the first node
            # Time: O(1), Space: O(1)

        self.length += 1  
        # Increase size of linked list because one node is added
        # Time: O(1), Space: O(1)

    def insert(self, index, value):
        # insert() adds a new node at a given index in the circular linked list
        # It returns:
        #   True  → if insertion is successful
        #   False → if index is invalid

        if index < 0 or index > self.length:
            # Invalid index
            raise Exception("index out of range")

        if index == 0:
            # Insert at beginning
            self.prepend(value)
            return True

        if index == self.length:
            # Insert at end
            self.append(value)
            return True

        # Insert in the middle

        new_node = Node(value)
        temp_node = self.head

        for _ in range(index - 1):
            # Traverse to node just before insertion point
            temp_node = temp_node.next

        new_node.next = temp_node.next
        # New node points to next node in list

        temp_node.next = new_node
        # Previous node now points to new node

        self.length += 1
        # Update length

        return True

    def traversal(self):
        # traversal() prints all values in the circular linked list
        # Since the list is circular, we must stop when we reach head again

        temp_node = self.head  
        # Start traversal from the head node
        # Time: O(1), Space: O(1)

        while temp_node is not None:
            # Loop runs until we manually break
            # We cannot rely on None in circular lists
            # Time: O(n), Space: O(1)

            print(temp_node.value)  
            # Print current node's value
            # Time: O(1), Space: O(1)

            temp_node = temp_node.next  
            # Move to the next node
            # Time: O(1), Space: O(1)

            if temp_node == self.head:
                # If we reached the head again
                # It means one full cycle is completed
                # Break to avoid infinite loop
                # Time: O(1), Space: O(1)
                break

            
    def search(self, value):
        # search() checks whether a given value exists in the circular linked list
        # It returns:
        #   True  → if value is found
        #   False → if value is not found

        temp_node = self.head  
        # Start searching from the head
        # Time: O(1), Space: O(1)

        while temp_node is not None:
            # Loop runs until we manually break
            # Time: O(n), Space: O(1)

            if temp_node.value == value:
                # If current node contains the searched value
                # Time: O(1), Space: O(1)

                return True  
                # Value found, stop search and return True

            temp_node = temp_node.next  
            # Move to the next node
            # Time: O(1), Space: O(1)

            if temp_node == self.head:
                # If we reached head again
                # Full circle completed and value not found
                break

        return False  
    
    # Value does not exist in the list
    def get(self, index):
        # get() returns the node present at a given index
        # It returns:
        #   Node object → if index is valid
        #   None        → if index is invalid
        # Special case:
        #   index = -1 returns the tail node

        current = self.head  
        # Start traversal from the head node
        # Time: O(1), Space: O(1)

        if index == -1:
            # Special shortcut for last node
            # We directly return tail instead of traversing
            # Time: O(1), Space: O(1)

            return self.tail

        if index < -1 or index >= self.length:
            # Invalid index:
            #  - less than -1
            #  - greater than or equal to length
            # Time: O(1), Space: O(1)

            return None

        for _ in range(index):
            # Move forward 'index' times to reach the desired node
            # Loop runs index times
            # Time: O(n), Space: O(1)

            current = current.next  
            # Move to the next node in the circular linked list
            # Time: O(1), Space: O(1)

        return current  
        # Return the node at the requested index
        # Time: O(1), Space: O(1)

    def set(self,index, value):
        target = self.get(index)
        if target:
            target.value = value
            return True
        return False

    def pop_first(self):
        # pop_first() removes and returns the head node
        # Returns:
        #   Node object → if list not empty
        #   None        → if list empty

        if self.length == 0:
            # Empty list case
            # Time: O(1), Space: O(1)
            return None

        pop_node = self.head
        # Store current head to return later
        # Time: O(1), Space: O(1)

        if self.length == 1:
            # Single node case → list becomes empty
            # Time: O(1), Space: O(1)
            self.head = None
            self.tail = None
        else:
            # Move head forward
            # Time: O(1), Space: O(1)
            self.head = self.head.next

            # Maintain circular property
            # Time: O(1), Space: O(1)
            self.tail.next = self.head

            # Detach removed node
            # Time: O(1), Space: O(1)
            pop_node.next = None

        self.length -= 1
        # Update length
        # Time: O(1), Space: O(1)

        return pop_node
        # Overall Time: O(1)
        # Overall Space: O(1)

    def pop(self):
        # pop() removes and returns the last node (tail)
        # Returns:
        #   Node object → if list not empty
        #   None        → if list empty

        if self.length == 0:
            # Empty list
            # Time: O(1), Space: O(1)
            return None

        pop_node = self.tail
        # Store current tail
        # Time: O(1), Space: O(1)

        if self.length == 1:
            # Single node case → list becomes empty
            # Time: O(1), Space: O(1)
            self.head = None
            self.tail = None
        else:
            # Traverse to node before tail
            # Time: O(n), Space: O(1)
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next

            # Update tail and maintain circular link
            # Time: O(1), Space: O(1)
            self.tail = temp
            self.tail.next = self.head

            pop_node.next = None
            # Detach removed node
            # Time: O(1), Space: O(1)

        self.length -= 1
        # Update length
        # Time: O(1), Space: O(1)

        return pop_node
        # Overall Time: O(n)
        # Overall Space: O(1)

    def remove(self, index):
        # remove() removes node at given index
        # Returns:
        #   Node object → if index valid
        #   None        → if index invalid

        if index < 0 or index >= self.length:
            # Invalid index
            # Time: O(1), Space: O(1)
            return None

        if index == 0:
            # Remove first node
            # Time: O(1), Space: O(1)
            return self.pop_first()

        if index == self.length - 1:
            # Remove last node
            # Time: O(n), Space: O(1)
            return self.pop()

        # Remove node from middle
        # Time: O(n), Space: O(1)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        remove_node = temp.next
        temp.next = remove_node.next
        remove_node.next = None

        self.length -= 1

        return remove_node

        # Overall Time: O(n)
        # Overall Space: O(1)

    def delete_all(self):
        self.tail.next = None 
        self.head = None
        self.tail = None
        self.length = 0 





new = CSLinked_List()
new.append(67)
new.append(676)
new.append(67788)
new.append(6777)
new.pop_first()
print(new)
print(new.tail)