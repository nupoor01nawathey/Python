#10 CHECK IF THE LIST IS SORTED OR NOT
# Tests to pass [1,2,3,4,5] [1,3,3,4,5]
# Tests to pass [1,3,2,4,5]

def check_if_sorted_list_1(l):
  k=0
  for i in range(len(l)-1):
    if(l[i] <= l[i+1]):
      pass
    else:
      k=1
      break
  return k==0 # returns bool True or False

print(check_if_sorted_list_1([1,2,3,4,5]))
print(check_if_sorted_list_1([1,3,3,4,5]))
print(check_if_sorted_list_1([1,3,2,4,5]))





def check_if_sorted_list_2(l):
  return all(l[i] <= l[i+1] for i in range(len(l)-1))

print(check_if_sorted_list_2([1,2,3,4,5]))
print(check_if_sorted_list_2([1,3,3,4,5]))
print(check_if_sorted_list_2([1,3,2,4,5]))