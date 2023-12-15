#6 Leader in an array

# The idea is to scan all the elements from right to left in an array and keep track of the maximum till now. 
# When the maximum changes its value, print it.

# Let the array be arr = {16, 17, 4, 3, 5, 2}
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 2 , ans[] = { 2 }
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 5 , ans[] = { 2, 5 }
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 5 , ans[] = { 2, 5 } 
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 5 , ans[] = { 2, 5 }
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 17 , ans[] = { 2, 5, 17 }
# arr[] = {16, 17, 4, 3, 5, 2} , max_from_right = 17 , ans[] = { 2, 5, 17 }


def find_leaders(l, l_size): 
  leaders=[]
  max_from_right=l[l_size-1]
  leaders.append(max_from_right)
  for i in range(len(l)-2, -1, -1):
    if max_from_right < l[i]:
      max_from_right=l[i]
      leaders.append(l[i])

  return leaders
  
print(find_leaders([16, 17, 4, 3, 5, 2], 6)) # [2, 5, 17]
print(find_leaders([1, 2, 3, 4, 5, 2], 6))   # [2, 5]


# Time Complexity: O(n)
# Auxiliary Space: O(1)
