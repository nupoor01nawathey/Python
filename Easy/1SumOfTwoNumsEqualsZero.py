#1 Output pair of numbers where sum of those two numbers is 0

# 1.
def sum_of_two_number_if_zero(l):
  if len(l)>1:
    x=[(i,j) for i in [i for i in l if i<0] for j in l if i+j==0]
    
    if len(x)>0:
      return x
    else:
      return "No pair found"
  
  else:
    return "lenght of input list is less than 2"
    
print(sum_of_two_number_if_zero([1,2,3,4,5,-1,-2,2,5,4])) # [(-1, 1), (-2, 2), (-2, 2)]
print(sum_of_two_number_if_zero([1,2,3,4])) # No pair found
print(sum_of_two_number_if_zero([1])) # lenght of input list is less than 2


# 2.
def sum_of_two_number_if_zero(l):
  out=[]
  if len(l)>1:
    for i in l:
      if i<0:
        for j in l:
          if i+j==0:
            out += [(i,j)]
    if len(out)>0:
      return out
    else:
      return "No pair found"
  else:
    return "lenght of input list is less than 2"

print(sum_of_two_number_if_zero([1,2,3,4,5,-1,-2,2,5,4])) # [(-1, 1), (-2, 2), (-2, 2)]
print(sum_of_two_number_if_zero([1,2,3,4])) # No pair found
print(sum_of_two_number_if_zero([1])) # lenght of input list is less than 2


