class Node: # Node class represents a single element in the linked list
    def __init__(self, data=None):
        self.data = data  # Initialize the data stored in the node
        self.next = None  # Initialize the reference to the next node


class OrderedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    # Check if the linked list is empty
    def is_empty(self):
        return self.head is None

    # Get the size of the linked list
    def size(self):
        current = self.head
        count = 0
        while current:  # Loop through the linked list until the end is reached
            count += 1  # Increment the counter
            current = current.next  # Move to the next node
        return count  # Return the size of the linked list

    # Search for a specific data in the linked list
    def search(self, data):
        current = self.head
        while current and current.data <= data:  # Loop until reaching the end or finding a node with data greater than the target
            if current.data == data:  # If the current node contains the target data
                return True  # Return True
            current = current.next  # Move to the next node
        return False  # Return False if the target data is not found

    # Add a new data to the linked list in sorted order
    def add(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.is_empty() or self.head.data > data:  # If the list is empty or the new data is smaller than the head
            new_node.next = self.head  # Set the next reference of the new node to the current head
            self.head = new_node  # Update the head to point to the new node
        else:
            current = self.head
            while current.next and current.next.data <= data:  # Loop to find the correct position to insert the new node
                current = current.next
            new_node.next = current.next  # Set the next reference of the new node
            current.next = new_node  # Insert the new node in the correct position

    # Remove a specific data from the linked list
    def remove(self, data):
        current = self.head  # Start from the head
        previous = None  # Initialize a reference to the previous node
        found = False  # Initialize a flag to indicate if the data is found
        while not found and current is not None:  # Loop until the data is found or the end of the list is reached
            if current.data == data:  # If the current node contains the data we want to remove
                found = True  # Set the flag to True
            elif current.data > data:  # If the data in the current node is greater than the target
                return  # Exit the loop as the element is not found because the list is ordered
            else:
                previous = current  # Update the reference to the previous node
                current = current.next  # Move to the next node

        if found:  # If the data is found
            if previous is None:  # If the data to be removed is at the head of the linked list
                self.head = current.next  # Update the head to point to the next node
            else:
                previous.next = current.next  # Update the reference from the previous node to skip the current node


    # Print the elements of the linked list
    def print_list(self):
        current = self.head  # Start from the head
        while current:  # Loop until reaching the end of the list
            print(current.data, end=' ')  # Print the data of the current node
            current = current.next  # Move to the next node
        print()  # Print a new line after printing all elements

# Create an instance of the ordered linked list
ordered_list = OrderedList()

# Add elements to the list
ordered_list.add(5)
ordered_list.add(1)
ordered_list.add(3)
ordered_list.add(7)
ordered_list.add(2)

# Print the list
ordered_list.print_list()  # Output: 1 2 3 5 7

# Check if an element is in the list
print(ordered_list.search(3))  # Output: True
print(ordered_list.search(6))  # Output: False

# Remove an element from the list
ordered_list.remove(3)
ordered_list.print_list()  # Output: 1 2 5 7
print(ordered_list.size())
