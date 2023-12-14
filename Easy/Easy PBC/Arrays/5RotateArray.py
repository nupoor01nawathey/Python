# 5 Reversal algorithm for Array rotation
# Given an array arr[] of size N, the task is to rotate the array by d position to the left.

# Examples: 
# Input:  arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3, 4, 5, 6, 7, 1, 2
# Explanation: If the array is rotated by 1 position to the left, 
# it becomes {2, 3, 4, 5, 6, 7, 1}.
# When it is rotated further by 1 position,
# it becomes: {3, 4, 5, 6, 7, 1, 2}

# Input: arr[] = {1, 6, 7, 8}, d = 3
# Output: 8, 1, 6, 7

lst = [1, 6, 7, 8]
def rotate_array_to_left(l, k):    
  return l[k:] + l[:k]
  
print(rotate_array_to_left(lst, 3))



def rotate_array_to_right(l, k):    
  k = k % len(l)
  
  left, right = 0, len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left, right = left+1, right-1

  left, right = 0, len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left, right = left+1, right-1

  left, right = 0, len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left, right = left+1, right-1
  return l
  
print(rotate_array_to_right(lst, 3))

