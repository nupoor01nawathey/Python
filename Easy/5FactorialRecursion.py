#5 RECURSION: FACTORIAL OF A GIVEN NUMBER

def factorial_1(n):
  if n <= 1:
    return 1
  else:
    return(n * factorial_1(n-1))

print(factorial_1(5))



def factorial_2(n):
  fact=1
  for i in range(n, 0, -1): # 0 will get excluded in range
    fact *= i
    print(i, fact)
  return fact

print(factorial_2(5))