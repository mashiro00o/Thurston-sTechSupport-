# insertion sort (quadratic) O(n^2)
def insertion_sort(A):
  for i in range(1, len(A)): # Iterate through the list starting from the second element, assuming the first item is already sorted.
    key = A[i]  # Store the current element to be inserted into the sorted list.
    j = i - 1  # Start comparing the key with the sorted list on the left.
    while j >= 0 and key < A[j]: # Move the items in the array to create space for the key in the sorted list.
      A[j+1] = A[j]  # Move each element to the right.
      j -= 1
    A[j+1] = key # Insert the key into its correct position in the sorted list.
  return A # Return the sorted list.

# main
data = [4, 12, 1, 5, 2, 8, 17] # Test the data with a sample list
print(insertion_sort(data)) # output [1, 2, 4, 5, 8, 12, 17]
