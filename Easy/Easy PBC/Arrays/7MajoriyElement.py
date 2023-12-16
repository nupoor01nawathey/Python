#6 Check for Majority Element in a sorted array

# Given an array arr of N elements,  A majority element in an array arr of size N is an element that appears more than N/2 times in the array. 
# The task is to write a function say isMajority() that takes an array (arr[] ), array’s size (n) and a number to be searched (x) as parameters and returns true if x is a majority element (present more than n/2 times).

# Examples: 
# Input: arr = [1, 2, 3, 3, 3, 3, 10], x = 3
# Output: True (x appears more than n/2 times in the given array)

# Input: arr = [1, 1, 2, 4, 4, 4, 6, 6], x = 4
# Output: False (x doesn't appear more than n/2 times in the given array)

# Input: arr = [1, 1, 1, 2, 2], x = 1
# Output: True (x appears more than n/2 times in the given array)


def find_majority_element(lst, n): 
  base_dict={}
  lst_size=len(lst)//2
  l1=[]
  for i in lst:
    if i in base_dict:
      base_dict[i]+=1
    else:
      base_dict[i]=1

    if base_dict[i] > lst_size and i==n:
      l1.append(i)
  
  if len(l1)>0:
    return True
  else:
    return False
  
print(find_majority_element([1, 2, 3, 3, 3, 3, 10], 3))
print(find_majority_element([1, 1, 2, 4, 4, 4, 6, 6], 4))


# Time Complexity: O(n)
# Auxiliary Space: O(1)

