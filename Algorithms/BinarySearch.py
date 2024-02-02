# binary search (iterative)  - (logarithmic) O(lg n)
def binary_search_iterative(A, target):
  low = 0
  high = len(A) - 1
  while low <= high: # still have items to search for
    mid = (low + high) // 2 # find the middle element or data
    if A[mid] == target: # data is the middle data
      return mid # data found
    elif target < A[mid]: # must be in the left half, ignore right half
      high = mid - 1
    else: # target > A[mid], must be in the right half, ignore left half
      low = mid + 1
  return 'data not found' # data not found

# binary search (recursive)
def binary_search_recursive(A, target, low, high):
  if low > high: # data not in the array / list
    return "data not found"
  mid = (low + high)//2 # find the middle data
  if A[mid] == target: # middle data is the target needed
    return mid
  elif A[mid] < target: # target in right half
    return binary_search(A, target, mid+1, high)
  else: # A[mid] > target, target in left half
    return binary_search(A, target, low, mid-1)

# main
data = [1, 2, 3, 5, 6, 7, 9, 10]
print(binary_search_iterative(data, 7)) # success return 5
print(binary_search_iterative(data, 8)) # failure return data not found
print(binary_search_recursive(data, 7, 0, len(data))) # success return 5
print(binary_search_resursive(data, 8, 0, len(data))) # failure return data not found
