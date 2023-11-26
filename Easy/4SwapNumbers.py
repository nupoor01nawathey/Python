#4 SWAPPING OF TWO NUMBER 

def swap_1(a,b):
  return b,a

print(swap_1(1,2))



def swap_2(a,b):
  c=a
  a=b
  b=c
  return (a,b)

print(swap_2(1,2))