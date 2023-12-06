# 2 Majority Element

# Find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 

# Examples : 
# Input : A[]={3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater than the half of the size of the array size. 

# Input : A[] = {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is greater than the half of the size of the array size.

def find_majority_element(lst):
  count_elements={}
  for i in range(len(lst)):
    if lst[i] in count_elements:
      count_elements[lst[i]]+=1
    else:
      count_elements[lst[i]]=1
  for k in count_elements:
    if count_elements[k] > len(lst)/2:
      return k
    else:
      return "No Majority Element"
  
print(find_majority_element([2, 2, 2, 2, 5, 5, 2, 3, 3])) # 2
print(find_majority_element([3, 3, 4, 2, 4, 4, 2, 4]))    # No Majority Element
