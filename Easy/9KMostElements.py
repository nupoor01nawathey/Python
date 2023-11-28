#9 FIND K MOST FREQUENT ELEMENT OF AN ARRAY
# [1,1,1,2,2,3], k=2
# [1,2]

def k_most_frequent_elemts(a, k):
  base_dict=dict()
  final_set=set()
  for i in a:
    if i in base_dict:
      base_dict[i]+=1
      if(base_dict[i] >= k):
        final_set.add(i) # 1 appears 3 times so if used here list.append then 1 will appear twice in the o/p
    else:
      base_dict[i]=1
      
  return list(final_set) # convert to list here

print(k_most_frequent_elemts([1,1,1,2,2,3], 2))


