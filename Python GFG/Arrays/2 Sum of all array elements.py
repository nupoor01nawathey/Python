# Python Program to Find Sum of Array

# Given an array of integers, find the sum of its elements.

# Examples:
# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6


def find_sum(arr):
  total=0
  for i in arr:
    total += i
  return total

print("Sum of all elements in an array ", find_sum([1, 2, 3]))
print("Sum of all elements in an array ", find_sum([1, 2, -3]))

# Time Complexity: O(N)
# Auxiliary Space: O(1)



print("Sum of all elements using sum method ", sum([1, 2, 3]))
print("Sum of all elements using sum method ", sum([1, 2, -3]))

# Time Complexity: O(N)
# Auxiliary Space: O(1)