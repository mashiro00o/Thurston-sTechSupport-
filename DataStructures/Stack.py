class Stack:
    def __init__(self):
        # Initialize an empty list to store the elements of the stack
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an element to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            # If the stack is empty, return None
            return None

    def size(self):
        # Return the number of elements in the stack
        return len(self.items)

# Example data:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.size())  # Output stack size

popped_item = stack.pop()
print(popped_item)  # Output popped item
print(stack.size())  # Output stack size after pop

# output
# 3
# 3
# 2
