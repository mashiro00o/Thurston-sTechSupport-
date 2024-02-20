class Queue:
    def __init__(self):
        # Initialize an empty list to store the elements of the queue
        self.items = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an element to the rear of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.items.pop(0)
        else:
            # If the queue is empty, return None
            return None

    def size(self):
        # Return the number of elements in the queue
        return len(self.items)

# Example data:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.size())  # Output queue size

dequeued_item = queue.dequeue()
print(dequeued_item)  # Output dequeued item
print(queue.size())  # Output queue size after dequeue

# Output
# 3
# 1
# 2
