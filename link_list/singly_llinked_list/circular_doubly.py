# from doubly import Node

class Node():
    def __init__(self, value):
        # Node constructor initializes a new node object
        # Each node contains:
        #   value → data stored in the node
        #   next  → reference to next node
        #   prev  → reference to previous node
        # Time: O(1), Space: O(1)

        self.value = value
        # Stores the actual data
        # Time: O(1), Space: O(1)

        self.next = None
        # Initially no next node is linked
        # Will be updated when node is inserted
        # Time: O(1), Space: O(1)

        self.prev = None
        # Initially no previous node is linked
        # Required for doubly linked structure
        # Time: O(1), Space: O(1)
    
    def __str__(self):
        # Defines how the node is printed
        # Returns string representation of value
        # Time: O(1), Space: O(1)

        return str(self.value)


class cd_linklist():
    def __init__(self):
        # Constructor for Circular Doubly Linked List
        # Initially list is empty
        # Time: O(1), Space: O(1)

        self.head = None
        # Head → first node of the list
        # None means list is empty
        # Time: O(1), Space: O(1)

        self.tail = None
        # Tail → last node of the list
        # Needed for efficient append operation
        # Time: O(1), Space: O(1)

        self.length = 0
        # Keeps track of number of nodes
        # Useful for boundary checks
        # Time: O(1), Space: O(1)


    def __str__(self):
        # Returns string representation of entire circular list
        # Traverses once through the list
        # Time: O(n), Space: O(n) (for string storage)

        result = ""
        # Stores final string output
        # Time: O(1), Space: O(1)

        temp = self.head
        # Start traversal from head
        # Time: O(1), Space: O(1)

        if self.head is None:
            # If list is empty, return empty string
            # Time: O(1), Space: O(1)
            return ""

        while True:
            # Traverse in circular manner
            # Loop runs once per node → O(n)
            # Time: O(n), Space: O(1)

            result += str(temp.value)
            # Add current node's value to result
            # Time: O(1), Space: O(1)

            temp = temp.next
            # Move to next node
            # Time: O(1), Space: O(1)

            if temp == self.head:
                # If we come back to head,
                # full circle is completed
                # Time: O(1), Space: O(1)
                break

            result += "<->"
            # Add separator between nodes
            # Time: O(1), Space: O(1)

        return result


    def append(self, value):
        # append() inserts a new node at the end (tail)
        # Maintains circular and doubly structure
        # Time: O(1), Space: O(1)

        new = Node(value)
        # Create new node object
        # Time: O(1), Space: O(1)

        if self.head is None:
            # Case 1: List is empty
            # First node becomes head and tail
            # Time: O(1), Space: O(1)

            self.head = new
            # Head points to new node
            # Time: O(1), Space: O(1)

            self.tail = new
            # Tail also points to same node
            # Time: O(1), Space: O(1)

            new.next = new
            # Since only one node,
            # next should point to itself (circular)
            # Time: O(1), Space: O(1)

            new.prev = new
            # Previous should also point to itself
            # Maintains doubly circular structure
            # Time: O(1), Space: O(1)

        else:
            # Case 2: List already has nodes
            # Insert new node after tail
            # Time: O(1), Space: O(1)

            self.tail.next = new
            # Old tail's next points to new node
            # Time: O(1), Space: O(1)

            new.prev = self.tail
            # New node's prev points to old tail
            # Time: O(1), Space: O(1)

            self.tail = new
            # Update tail to new node
            # Time: O(1), Space: O(1)

            self.head.prev = self.tail
            # Head's prev must point to new tail
            # Maintains circular doubly link
            # Time: O(1), Space: O(1)

            self.tail.next = self.head
            # Tail's next must point to head
            # Completes circular structure
            # Time: O(1), Space: O(1)

        self.length += 1
        # Increase size of list
        # Important for size tracking
        # Time: O(1), Space: O(1)
    
    def prepend(self, value):
        # prepend() inserts a new node at the beginning (head)
        # In Circular Doubly Linked List:
        #   - New node becomes the new head
        #   - Tail must still connect to head (circular property)
        # Time: O(1), Space: O(1)

        new = Node(value)
        # Create a new node object with given value
        # Time: O(1), Space: O(1)

        if self.length == 0:
            # Case 1: If list is empty
            # First node becomes both head and tail
            # Time: O(1), Space: O(1)

            self.head = new
            # Head points to new node
            # Time: O(1), Space: O(1)

            self.tail = new
            # Tail also points to same node
            # Time: O(1), Space: O(1)

            new.next = new
            # Since only one node, next should point to itself
            # Maintains circular structure
            # Time: O(1), Space: O(1)

            new.prev = new
            # Previous also points to itself
            # Maintains doubly circular property
            # Time: O(1), Space: O(1)

        else:
            # Case 2: List already has nodes
            # Insert new node before current head
            # Time: O(1), Space: O(1)

            new.next = self.head
            # New node's next should point to old head
            # Time: O(1), Space: O(1)

            self.head.prev = new
            # Old head’s prev should point to new node
            # Time: O(1), Space: O(1)

            new.prev = self.tail
            # New node’s prev should point to tail
            # Because in circular list, head.prev = tail
            # Time: O(1), Space: O(1)

            self.tail.next = new
            # Tail’s next must point to new head
            # Maintains circular connection
            # Time: O(1), Space: O(1)

            self.head = new
            # Update head reference to new node
            # Time: O(1), Space: O(1)

        self.length += 1
        # Increase size of list after insertion
        # Time: O(1), Space: O(1)

    def traversal(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
        
    def reverse_traversal(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp == self.head:
                break

    def search(self,value):
        temp = self.head 
        index = 0 
        while temp:
            # index +=1
            if temp.value == value:
                return index
            index +=1
            temp=temp.next
            if temp == self.head:
                break
        return False


new_cdll = cd_linklist()
new_cdll.append(13)
new_cdll.append(134)
new_cdll.append(156)
new_cdll.prepend(9999)
print(new_cdll.search(1345))