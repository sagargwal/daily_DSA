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

    def insert(self,index,value):
        new_node = Node(value)
        temp_node = self.head
        if self.length == 0:
            self.head = temp_node
            self.tail = temp_node
            new_node.next = new_node
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:   
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1 

new = CSLinked_List()
new.insert(0,78)
# new.append(89)
# new.prepend(6777)
print(new)