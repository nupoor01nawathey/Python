#2 FIND A NON - NEGATIVE INTEGER THAT IS NOT IN THE ARRAY
# Given numbers in the list are sorted in ascending order


l=[0,1,3,4,5,7,8,9]

# Generate sample_list based on the max value from the given list using range
# Next iterate over this sample_list and check if each element is present in the given list
def non_negative_absent_from_array(l):    
  if len(l)<1:
    return False
  sample_list=[]
  for i in range(max(l)+1):
    sample_list.append(i)
  not_available=[]
  for j in sample_list:
    if j not in l:
      print('value is not present in the output',j)
      not_available.append(j)
  return not_available

print(non_negative_absent_from_array(l))
