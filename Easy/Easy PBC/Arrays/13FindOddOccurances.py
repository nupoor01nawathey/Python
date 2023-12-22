# 13 Find the two numbers with odd occurrences in an unsorted array

# Given an unsorted array that contains even number of occurrences for all numbers except two numbers. 
# Find the two numbers which have odd occurrences in O(n) time complexity and O(1) extra space.

# Input: {12, 23, 34, 12, 12, 23, 12, 45}
# Output: 34 and 45

# Input: {4, 4, 100, 5000, 4, 4, 4, 4, 100, 100}
# Output: 100 and 5000

# Input: {10, 20}
# Output: 10 and 20

def find_two_numbers_with_odd_occurances(A):
  base_dict={}
  l1=[]
  for i in A:
    if i in base_dict:
      base_dict[i]+=1
    else:
      base_dict[i]=1
      
  for k in base_dict:
    if(base_dict[k]%2 != 0 ):
      l1.append(k)
  return l1


print(find_two_numbers_with_odd_occurances([12, 23, 34, 12, 12, 23, 12, 45])) # [34, 45]
print(find_two_numbers_with_odd_occurances([4, 4, 100, 5000, 4, 4, 4, 4, 100, 100])) # [100, 5000]
print(find_two_numbers_with_odd_occurances([10,20])) # [10, 20]

# Time Complexity: O(N)
# Auxiliary Space: O(N), using the list will require extra space


