#6 COUNT OF ELEMENTS IN A LIST

def find_lenghth_of_list(l):
  cnt=0
  for i in l:
    cnt=cnt+1
  return cnt

print(find_lenghth_of_list([]))
print(find_lenghth_of_list([1,2,3]))
print(find_lenghth_of_list([0]))
