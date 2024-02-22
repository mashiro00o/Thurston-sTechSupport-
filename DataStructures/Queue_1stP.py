# Queaue - FIFO (first in first out)
# using first principles and front and rear

# Initialize the size of the queue
N = 6

# Initialize the queue with None values
queue = [None for i in range(N)] # queue can hold N-1 items

# Initialize the front and rear pointers
front = -1 # index where next item is to be deleted
rear = 0 # index where next item is to be inserted

# Function to enqueue (insert) an item into the queue
def enqueue(item):
  global rear, front
  if is_full(): # Check if the queue is full
    print("Queue full")
  else: # If not full
    queue[rear] = item # Insert the item at the rear position
    rear = (rear + 1) % N # Update rear pointer to the next position
    print(item, "inserted")
    if is_empty(): # Update front when queue is empty
      front = (front + 1) % N

# Function to dequeue (remove) an item from the queue
def dequeue():
  global front, rear
  if is_empty(): # Check if the queue is empty
    return "Queue empty"
  else:
    item = queue[front] # Get the item at the front of the queue
    queue[front] = None # Remove the item by setting its position to None
    front = (front + 1) % N # Update front pointer to the next position
    if rear == front: # If last item was removed, reset front and rear
      front = -1
      rear = 0
    return str(item) + " deleted"

# Function to check if the queue is full
def is_full():
  return size() == N - 1  # If the size of the queue is equal to N - 1, it's full

# Function to check if the queue is empty
def is_empty():
  return front == -1  # If front pointer is at -1, the queue is empty

# Function to get the current size of the queue
def size():
  if is_empty():  # If the queue is empty, size is 0
    return 0
  elif front < rear:  # If the queue doesn't wrap around
    return rear - front
  else:  # If the queue wraps around
    return N - (front - rear)

# main
print(queue, size())  
enqueue(1)  
enqueue(2)  
enqueue(3)  
enqueue(4)  
enqueue(5) 
enqueue(6)  
print(queue, size())  
print(dequeue(), size())  
print(dequeue(), size())  
print(dequeue(), size())  
print(queue, size())  
print(dequeue(), size())  
print(dequeue(), size())  
print(dequeue(), size())  
print(queue, size())  
