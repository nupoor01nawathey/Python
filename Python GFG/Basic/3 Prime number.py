# Python program to check if input number is prime or not

# The idea to solve this problem is to iterate through all the numbers starting from 2 to (N/2) using a for loop 
# and for every number check if it divides N. If we find any number that divides, we return false. 
# If we did not find any number between 2 and N/2 which divides N then it means that N is prime and we will return True.

n=int(input())

def is_prime(n):
  if n==1:
    return False
  else:
    for i in range(2, int(n/2)+1):
      if n%i==0:
        return False
      else:
        return True
    
print(is_prime(n))