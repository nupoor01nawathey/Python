# Python Program for array left rotation by d positions.

# Input arr[] = [1, 2, 3, 4, 5, 6, 7, 8], d = 2, size = 8

# Output
# Original array: [1, 2, 3, 4, 5, 6, 7, 8]
# Rotated array:  [3, 4, 5, 6, 7, 8, 1, 2]


# Approach
# 1) Store d elements in a temp array
#   temp[] = [1, 2]
# 2) Shift rest of the arr[]
#   arr[] = [3, 4, 5, 6, 7, 8, 7, 8]
# 3) Store back the d elements
#   arr[] = [3, 4, 5, 6, 7, 8, 1, 2]

def left_rotate(arr, d):
  tmp=[]
  i=0
  while(i<d):
    tmp.append(arr[i])
    i+=1
  i=0
  while(d < len(arr)):
    arr[i]=arr[d]
    d+=1
    i+=1
  arr[:]=arr[:i]+tmp
  return arr  

print(left_rotate([1, 2, 3, 4, 5, 6, 7, 8], 2))

# Time complexity: O(n) 
# Auxiliary Space: O(d)




arr1=[1, 2, 3, 4, 5, 6, 7, 8]
d=2
print("Left rotate array using array slicing ", arr1[d:len(arr1)]+arr1[0:d])
# Time complexity : O(n) where n is size of given array
# Auxiliary Space : O(1)



