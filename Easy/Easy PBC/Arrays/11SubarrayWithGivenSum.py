#11 Find Subarray with given sum | Set 1 (Non-negative Numbers)

# Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.
# Note: There may be more than one subarray with sum as the given sum, print first such subarray. 

# Examples: 
# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
# Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Output: Sum found between indexes 1 and 4
# Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7

# Input: arr[] = {1, 4}, sum = 0
# Output: No subarray found
# Explanation: There is no subarray with 0 sum

# Idea is to store current_sum, i in the base_dict. This way we can have total sum and index and check this total sum against the expected sum
def find_subarray_with_given_sum(l, expected_sum):    
  base_dict = {}
  current_sum=0
  for i in range(len(l)):
    current_sum += l[i]
    if current_sum==expected_sum:
      return i
    if current_sum-expected_sum in base_dict:
      return base_dict[current_sum-expected_sum]+1, i
    base_dict[current_sum]=i
    
print(find_subarray_with_given_sum([1, 4, 20, 3, 10, 5], 33))
print(find_subarray_with_given_sum([1, 4, 0, 0, 3, 10, 5], 7))
print(find_subarray_with_given_sum([1, 4], 0))


# Time Complexity: O(N)
# Auxiliary Space: O(N) 
