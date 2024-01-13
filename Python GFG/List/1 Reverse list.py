# Reversing a list using two-pointer approach

def reverse_list(arr):
  left=0
  right=len(arr)-1
  while(left<right):
    tmp=arr[left]
    arr[left]=arr[right]
    arr[right]=tmp
    left+=1
    right-=1
  return arr
  
arr = [1, 2, 3, 4, 5, 6, 7]
print("Original list ", arr)
print("Reversed list ", reverse_list(arr))

# Time Complexity: O(N)
# Auxiliary Space: O(1)