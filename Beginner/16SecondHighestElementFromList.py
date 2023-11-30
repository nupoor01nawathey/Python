#16 GET THE SECOND GREATEST ELEMENT FROM THE ARRAY


def second_smallest_element(l, l_size):
  if l_size < 2:
    return(" Invalid Input ")
  
  first = second = -2147483648
  for i in range(l_size):
    # If current element is smaller than first then update both first and second 
    if (l[i] > first):
      second=first
      first=l[i]
    # If l[i] is in between first and second then update second      
    elif (l[i] > second and l[i] != first):
      second=l[i]
      
  if (second == -2147483648):
    return("There is no second largest element")
  else:
    return("The second largest element is", second)

print(second_smallest_element([11,2,3,2,3,4,9,1,5], 9))


# Big O 
# O(N) Where N is size of input list
# O(1) as no extra space is required to find the output
