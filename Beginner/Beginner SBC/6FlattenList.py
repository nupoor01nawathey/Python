#6 Flatten a list and count occurrences | Accenture

l = [[1,2], [3,4], [2,3], [5,1], [7,1,2]]


def flatten_and_count_list_elements_1(l):
  base_dict=dict()
  for i in l:
    for j in i:
      if j in base_dict:
        base_dict[j]+=1
      else:
        base_dict[j]=1
  return base_dict
  
print(flatten_and_count_list_elements_1(l))



def flatten_and_count_list_elements_2(l):
  staging_lst=[]
  [staging_lst.extend(i) for i in l]
  b = { item:staging_lst.count(item) for item in set(staging_lst)}
  return b
  
print(flatten_and_count_list_elements_2(l))