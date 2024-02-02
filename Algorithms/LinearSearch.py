# Linear search using for-loop
def linear_search_for(A, target):
  for i in range(len(A)):
    if A[i] == target: # data was found
      return 'data found'
  return 'data not found'

# Linear search using while-loop
def linear_search_while(A, target):
  i = 0
  while i < len(A):
    if A[i] == target: # data was found
      return 'data found'
    i += 1
  return 'data not found'

# Main
name = ['John', 'Mary', 'Tim', 'Alice']
print(linear_search_for(name, 'Tim')) # found
print(linear_search_for(name, 'Grace')) # not found
print(linear_search_while(name, 'John')) # found
print(linear_search_while(name, 'Andy')) # not found
