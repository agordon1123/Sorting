# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i

  return -1 # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  if len(arr) == 0:
    return -1 # array empty
  
  # if num is outside limits of sorted arr
  if target > arr[high] or target < arr[low]:
    return -1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    elif arr[mid] > target:
      high = mid - 1

  # return -1 if None
  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high) // 2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
