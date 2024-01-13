# Remove multiple elements from a list in Python

# Given a list of numbers, write a Python program to remove multiple elements from a list based on the given condition.

# Example: 

# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

# Input: [11, 5, 17, 18, 23, 50]
# Output: Remove = [1:5], New_list = [11, 50]


lst1=[12, 15, 3, 10]
unwanted_lst=[12, 3]

lst2=[]
for i in lst1:
  if i not in unwanted_lst:
    lst2.append(i)
print(lst2)


# short code for above
lst2 = [i for i in lst1 if i not in unwanted_lst]
print(lst2)

# Time Complexity: O(N)
# Auxiliary Space: O(N)