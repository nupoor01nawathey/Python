# 1 Check if pair with given Sum exists in Array (Two Sum)

# Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 

# Examples: 
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation:  If we calculate the sum of the output,1 + (-3) = -2
# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No


# Approach
# Store array/list elements in a dictionary with corresponding index
# x+y=target_sum => x = target_sum - y
# While iterating check for complimentary element by checking if element already exists or not
def twoSum(lst, lst_size, target_sum):
  base_dict={}
  for i in range(lst_size):
    if lst[i] in base_dict:
      return [i,base_dict[lst[i]]]
    else:
      base_dict[target_sum - lst[i]] = i

A = [1, 4, 45, 6, 0, -1, 2, 4, 10, 6, 8]
n = 16
print(twoSum(A, len(A), n))

B = [0, -1, 2, -3, 0, 1]
t = -2
print(twoSum(B, len(B), t))


# Time Complexity: O(N), As the whole array is needed to be traversed only once.
# Auxiliary Space: O(N), A hash map has been used to store array elements.

