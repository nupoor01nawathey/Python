#14 Narcissist Number
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 (pow of 4 as length of 1634 is 4)

import math
def find_narcissist_number_1(n):
  s=0
  n_to_str=str(n)
  for i in n_to_str:
    s += math.pow(int(i), len(n_to_str))
  if s==n:
    return True
  else:
    return False

print(find_narcissist_number_1(1634)) # True 
print(find_narcissist_number_1(1234)) # False




def find_narcissist_number_2(n):
  n_to_str=str(n)
  return "True" if (sum([math.pow(int(i), len(n_to_str)) for i in n_to_str])) == n else "False"
  
print(find_narcissist_number_2(1634)) # True 
print(find_narcissist_number_2(1234)) # False