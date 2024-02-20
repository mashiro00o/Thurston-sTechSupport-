class Node: # Node class represents a single element in the linked list
    def __init__(self, data):
        self.data = data  # Initialize the data stored in the node
        self.next = None  # Initialize the reference to the next node


class UnorderedLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list to None

    # Check if the linked list is empty
    def is_empty(self):
        return self.head is None

    # Add a new item to the beginning of the linked list
    def add(self, item):
        new_node = Node(item)  # Create a new node with the given item
        new_node.next = self.head  # Set the next reference of the new node to the current head
        self.head = new_node  # Update the head to point to the new node

    # Get the size of the linked list
    def size(self):
        count = 0  # Initialize a counter
        current = self.head  # Start from the head of the linked list
        while current is not None:  # Loop through the linked list
            count += 1  # Increment the counter
            current = current.next  # Move to the next node
        return count  # Return the size of the linked list

    # Search for a specific item in the linked list
    def search(self, item):
        current = self.head  # Start from the head of the linked list
        while current is not None:  # Loop through the linked list
            if current.data == item:  # If the current node contains the item we're looking for
                return True  # Return True
            current = current.next  # Move to the next node
        return False  # Return False if the item is not found

    # Remove a specific item from the linked list
    def remove(self, item):
        current = self.head  # Start from the head of the linked list
        previous = None  # Initialize a reference to the previous node
        found = False  # Initialize a flag to indicate if the item is found
        while not found and current is not None:  # Loop until the item is found or the end of the list is reached
            if current.data == item:  # If the current node contains the item we're looking for
                found = True  # Set the flag to True
            else:
                previous = current  # Update the reference to the previous node
                current = current.next  # Move to the next node

        if found:  # If the item is found
            if previous is None:  # If the item to be removed is the head of the linked list
                self.head = current.next  # Update the head to point to the next node
            else:
                previous.next = current.next  # Update the reference from the previous node to skip the current node

    # Display the elements of the linked list
    def display(self):
        current = self.head  # Start from the head of the linked list
        while current is not None:  # Loop through the linked list
            print(current.data, end=" ")  # Print the data of the current node
            current = current.next  # Move to the next node
        print()  # Print a new line after displaying all elements


# Usage example:
my_list = UnorderedLinkedList()

my_list.add(5)
my_list.add(3)
my_list.add(7)
my_list.add(2)
my_list.display()  # Output: 2 7 3 5

print(my_list.size())  # Output: 4

print(my_list.search(7))  # Output: True
print(my_list.search(4))  # Output: False

my_list.remove(3)
my_list.display()  # Output: 2 7 5
