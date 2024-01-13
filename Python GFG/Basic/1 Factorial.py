num=int(input())

def factorial_iterative(num):
  if num<0:
    return 0
  if num==0 or num==1:
    return 1
  else:
    fact=1
    while num>1:
      fact *= num
      num-=1
  return fact
  
print(factorial_iterative(num))



def factorial_recursive(num):
  return 1 if (num==1 or num==0) else num * factorial_recursive(num - 1) 
  
print(factorial_recursive(num))

