# Python program to find second largest number in a list
# Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.

# Examples: 

# Input: list1 = [10, 20, 4]
# Output: 10

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70


def findSecondLargest(arr):
  second=0
  largest=min(arr)
  for i in range(len(arr)):
    if arr[i]>largest:
      second=largest
      largest=arr[i]
    else:
      second=max(second, arr[i])
  return second

# Calling above method over this array set
print(findSecondLargest([10, 20, 4, 45, 99]))


# Time Complexity: O(N)
# Auxiliary Space: O(1)