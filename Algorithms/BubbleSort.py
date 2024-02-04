# bubble sort (non-optimised) O(n^2) - quadratic
def bubble_sort_non_optimised(A):
  n = len(A) # Get the length of the input list.
  for i in range(n): # Iterate through each element in the list.
    for j in range(n-1): # Iterate through the list elements from the beginning to the second-to-last element.
      if A[j] > A[j+1]: # Compare adjacent elements and swap them if they are in the wrong order.
        A[j], A[j+1] = A[j+1], A[j]
  return A # Return the sorted list.

# bubble sort using for-loop (optimised)
def bubble_sort_optimised_for(A):
  n = len(A) # Get the length of the input list.
  for i in range(n): # Iterate through each element in the list.
    swapped = False  # Assume the list is already sorted for optimization.
    for j in range(n-1): # Iterate through the list elements up to the second-to-last element.
      if A[j] > A[j+1]: # Compare adjacent elements and swap them if they are in the wrong order.
        A[j], A[j+1] = A[j+1], A[j]
        swapped = True  # Indicate that a swap has occurred.
    if not swapped: # If no swap occurred in the last pass, the list is already sorted, and the algorithm can exit early.
      break
    n -= 1 # Reduce the range of elements to consider in the next pass, as the last element is now sorted.
  return A # Return the sorted list.

# bubble sort using while-loop (optimised)
def bubble_sort_optimised_while(A):
  n = len(A) # Get the length of the input list.
  i = 0    
    while i < n: # Iterate while there are elements left to traverse.
      swapped = False  # Assume the list is already sorted for optimization.
      j = 0
      while j < n-1: # Iterate through the list elements up to the second-to-last element.
        if A[j] > A[j+1]: # Compare adjacent elements and swap them if they are in the wrong order.
          A[j], A[j+1] = A[j+1], A[j]
          swapped = True  # Indicate that a swap has occurred.
        j += 1
    if not swapped: # If no swap occurred in the last pass, the list is already sorted, and the algorithm can exit early.
      break
    n -= 1 # Reduce the range of elements to consider in the next pass, as the last element is now sorted.
    i += 1
  return A  # Return the sorted list.

# main
data = [4, 7, 1, 5, 2, 8, 3] # test the function with a unsorted list
print(bubble_sort_non_optimised(data)) # output [1, 2, 3, 4, 5, 7, 8]
print(bubble_sort_optimised_for(data)) # output [1, 2, 3, 4, 5, 7, 8]
print(bubble_sort_optimised_while(data)) # output [1, 2, 3, 4, 5, 7, 8]
