#11 Count the Frequency of Elements in a List

def count_frequency_of_elements(l):
  base_dict=dict()
  for i in l:
    if i in base_dict:
      base_dict[i]+=1
    else:
      base_dict[i]=1
  return base_dict
  
print(count_frequency_of_elements([1,2,3,4,5]))
print(count_frequency_of_elements([1,3,3,4,5]))
print(count_frequency_of_elements([1]))


