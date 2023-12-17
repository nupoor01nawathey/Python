#7 Segregate 0s and 1s in an array

# You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. Traverse array only once. 

# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 


def segregate_zeros_and_ones(lst, l_size): 
  left, right = 0, l_size-1
  while left<right:

    # Increment left index while we see 0 at left 
    while lst[left] == 0  :
      left += 1
      
    # Decrement right index while we see 1 at right 
    while lst[right] == 1 :
      right -= 1
    
    # If left is smaller than right then there is a 1 at left 
    # and a 0 at right. Exchange lst[left] and lst[right]
    if left < right:
      lst[left]=0
      lst[right]=1
      left += 1
      right -= 1
      print(left, right, lst[left], lst[right])
  return lst  
      

print(segregate_zeros_and_ones([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]  , 10))
print(segregate_zeros_and_ones([0, 1, 0, 1, 1, 1], 6))
  
# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Another approach is to count 0s and subtract from total length to get count of 1s
# Iterate according to the count for 0 and 1 

