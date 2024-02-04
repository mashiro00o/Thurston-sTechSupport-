# Define the quicksort function that takes a list A as input and returns the sorted list.
def quicksort(A):
  if len(A) <= 1: # Base case: if the list has 1 or fewer elements, it is already sorted.
    return A
  
  pivot = A[len(A) // 2] # Choose the pivot element as the middle element of the list. midpoint
  # Initialize empty lists to store elements less than, equal to, and greater than the pivot.
  left = []
  middle = []
  right = []
  
  for element in A: # Iterate through each element in the input list A.
    # Compare the element with the pivot and place it in the appropriate list.
    if element < pivot:
      left.append(element)
    elif element == pivot:
      middle.append(element)
    else: # if element > pivot
      right.append(element)

  # Recursively apply quicksort to the left and right sublists and concatenate the results.
  return quicksort(left) + middle + quicksort(right)

# main
data = [4, 7, 1, 5, 2, 8, 3] # Test data set
print(quicksort(data))
