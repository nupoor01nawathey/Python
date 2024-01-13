# Given a number x, determine whether the given number is Armstrong number or not. 
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
# Example:

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

# Input : 120
# Output : No
# 120 is not a Armstrong number.
# 1*1*1 + 2*2*2 + 0*0*0 = 9

n=int(input())

def check_armstrong_number_iterative_approach(n):
  total=0
  for i in str(n):
    total+=int(i) * int(i) * int(i)
  if total==n:
    return "Armstrong number"
  else:
    return "Not an armstrong number"

print(check_armstrong_number_iterative_approach(n))


def check_armstrong_number(n):
  sum=0
  l=len(str(n))
  for digit in str(n):
    sum += int(digit)**l
  if n==sum:
    return True
  else:
    return False
  
print(check_armstrong_number(n))


# Time complexity: O(n), wheer n is length of number
# Auxiliary Space: O(1)

