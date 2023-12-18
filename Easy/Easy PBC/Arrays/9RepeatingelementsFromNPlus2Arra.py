#9 Find the two repeating elements in a given array

# Given an array arr[] of N+2 elements. All elements of the array are in the range of 1 to N. 
# And all elements occur once except two numbers which occur twice. Find the two repeating numbers. 


# Input: arr = [4, 2, 4, 5, 2, 3, 1], N = 5
# Output: 4 2
# Explanation: The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.

# Input: arr = [2, 1, 2, 1, 3], N = 3
# Output: 1 2
# Explanation: The above array has n + 2 = 5 elements with all elements occurring once except 1 and 2 which occur twice. So the output should be 1 2.


def repeating_elements_from_n_plus_list(lst, l_size): 
  count=[0] * l_size
  for i in range(0, l_size):
    if count[lst[i]] == 1:
      print(lst[i], end=" ")
    else:
      count[lst[i]]+=1
      
print(repeating_elements_from_n_plus_list([4, 2, 4, 5, 2, 3, 1], 7))


# Time Complexity: O(n)
# Auxiliary Space: O(1)
