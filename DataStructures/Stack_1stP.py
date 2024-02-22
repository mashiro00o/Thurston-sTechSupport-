# Stack - LIFO (last in first out) reverse property
# using first principles and top

# Initialize the size of the stack
N = 5

# Initialize the stack with None values
stack = [None for i in range(N)]
top = -1  # Initialize top pointer to -1

# Function to push (insert) an item onto the stack
def push(item):
  global top
  if is_full():  # Check if the stack is full
    print("Stack full")
  else:  # If not full
    top += 1  # Increment top pointer
    stack[top] = item  # Insert the item at the top of the stack
    print(item, "inserted")

# Function to pop (remove) an item from the stack
def pop():
  global top
  if is_empty():  # Check if the stack is empty
    return "Stack empty"
  else:
    item = stack[top]  # Get the item at the top of the stack
    stack[top] = None  # Remove the item by setting its position to None
    top -= 1  # Decrement top pointer
    return str(item) + " deleted"

# Function to check if the stack is full
def is_full():
  return top == N - 1  # If the top pointer is at the last index, the stack is full

# Function to check if the stack is empty
def is_empty():
  return top == -1  # If the top pointer is at -1, the stack is empty

# Function to get the current size of the stack
def size():
  return top + 1  # The size of the stack is the index of the top element plus one

# main
push(1)  
push(2)  
push(3)  
push(4)  
push(5)  
push(6)  
print(pop())  
print(pop())  
print(pop())  
print(pop())  
print(pop())  
print(pop()) 
print(size())  
