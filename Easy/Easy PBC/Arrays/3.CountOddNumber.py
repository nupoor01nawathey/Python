# 3 Find the Number Occurring Odd Number of Times

# Given an array of positive integers. All numbers occur an even number of times except one number which occurs an odd number of times. Find the number in O(n) time & constant space.

# Examples : 

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
# Output : 3

# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5


def find_number_odd_times(lst):
  counter_dict={}
  for i in range(len(lst)):
    if lst[i] in counter_dict:
      counter_dict[lst[i]]+=1
    else:
      counter_dict[lst[i]]=1
  for k in counter_dict:
    if counter_dict[k]%2!=0:
      return k
  return -1
  
print(find_number_odd_times([1, 2, 3, 2, 3, 1, 3]))
print(find_number_odd_times([5, 7, 2, 7, 5, 2, 5]))

# Time Complexity: O(n)
# Auxiliary Space: O(n)