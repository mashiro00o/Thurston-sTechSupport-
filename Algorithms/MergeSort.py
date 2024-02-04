# merge sort (linearithmic) O(n lg n)
def merge_sort(A):
  if len(A) <= 1: # Base case: if the list has 1 or fewer elements, it is already sorted.
    return A

  # Split the list into two halves.
  mid = len(A) // 2
  left_half = A[:mid]
  right_half = A[mid:]

  # Recursively apply merge_sort to the left and right halves.
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  # Merge the sorted left and right halves.
  return merge(left_half, right_half)

# merge function that merges two sorted lists into a single sorted list.
def merge(left_half, right_half):
  i = j = 0
  merged_list = []
  while i < len(left_half) and j < len(right_half): # Compare elements from both lists and merge them into a single sorted list.
    if left_half[i] < right_half[j]:
      merged_list.append(left_half[i])
      i += 1
    else: # if left_half[i] > right_half[j]
      merged_list.append(right_half[j])
      j += 1

  # If there are remaining elements in either the left or right list, add them to the merged list.
  merged_list += left_half[i:]
  merged_list += right_half[j:]
  return merged_list # Return the merged list.

# main
data = [4, 7, 1, 5, 2, 8, 3] # Test data set
print(merge_sort(data)) # output [1, 2, 3, 4, 5, 7, 8]
