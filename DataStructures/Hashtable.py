# Hash table
def hash(key):
  return key % N

# Insert a key-value pair into the hash table
def insert(key, value):
  index = hash(key)
  if hash_table[index] == -1: # Check if the slot is available
    hash_table[index] = value # No collision, insert directly
  else: # Collision occurred
    i = (index + 1) % N # Linear probing to find the next available slot
    while hash_table[i] != -1: # Find the next free slot
      i = (i + 1) % N # Ensure within the range of the table
    hash_table[i] = value # Insert the collided record

# Search for a key in the hash table
def search(key, target):
  index = hash(key)
  if hash_table[index] == -1: # Check if the slot is empty
    return "Record not found"
  elif hash_table[index] != target: # Collided record
    i = (index + 1) % N
    while hash_table[index] != -1: # Search through collided records
      if hash_table[i] == target:
        return "Found in collided records"
      i = (i + 1) % N
    return "Not found in collided records"
  else: # Non-collision record
    return hash_table[index]

# Update the value associated with a key in the hash table
def update(key, target):
  # Search for the key, if found, update the value, else return error
  result = search(key, target)
  if result == "Record not found":
    return result
  elif result == 'Found in collided records':
    return 'Cannot update collided records'
  else:
    index = hash(key)
    hash_table[index] = target
    return 'Record updated successfully'

# Delete a key-value pair from the hash table
def delete(key):
  # Search for the key, if found, delete the record, else return error
  result = search(key, None)
  if result == 'Record not found':
    return result
  elif result == 'Found in collided records':
    return 'Cannot delete collided record'
  else:
    index = hash(key)
    hash_table[index] = -1 # Mark the slot as empty
    return 'Record deleted successfully'


# main
N = 10 # Size of hash table
hash_table = [] # Initialize empty list
for i in range(N):
  hash_table.append(-1)
print(hash_table)

# Records to be inserted into the hash table
records = {1234:'Tom', 651:'Mary', 238:'Ali'}

# Insert records into the hash table
for key, value in records.items():
  insert(key, value)
print(hash_table)

# Additional records insertion
insert(7654, 'Alex')
insert(999, 'MrPang')
insert(9, 'MsChen')
print(hash_table)

# Test search function
print(search(3, 'Peter')) # Output record not found (as key doesn't exist)
print(search(7654, 'Alex')) # Output found in collided records

print(search(1234, 'Tom')) # Output Tom

# Test update function
print(update(1234, 'New Tom')) # Output Record updated successfully
print(hash_table)

# Test delete function
print(delete(1234)) # Output Record deleted successfully
print(hash_table)
