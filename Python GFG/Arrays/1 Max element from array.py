# Python Program to Find Largest Element in an Array

# Given an array, find the largest element in it.

# Input : arr[] = {10, 20, 4}
# Output : 20
# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100


def find_largest_element(arr):
  assumed_max=arr[0]
  for i in range(1, len(arr)):
    if arr[i]>assumed_max:
      assumed_max=arr[i]
  return assumed_max

print("Largest in given array ", find_largest_element([10, 20, 4]))
print("Largest in given array ", find_largest_element([20, 10, 20, 4, 100]))

# Time Complexity: O(N)
# Auxiliary Space: O(1)



print("Largest in given array using max function ", max([10, 20, 4]))
print("Largest in given array using max function ", max([20, 10, 20, 4, 100]))

# Time Complexity: O(N)
# Auxiliary Space: O(1)