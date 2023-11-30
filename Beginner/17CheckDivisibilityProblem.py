#17 Find if given number is divisible by each of its digits

# N = 15
# Output: true (15 is divisible by 1 and 5)

# N = 123
# Output: true (123 is divisible by 1, 2 and 3)

# N = 143
# Output: false (143 is not divisible by 4 and 3)

# Approach:
# Get all the digits of the given number
# For each digit check if number%digit==0 (means divisible). 
# If any of them is non zero return false.
# If for all digits number%digit==0, return true.
# Consider divide by 0 case as well

def divisibility_check(num):    
  tmp=num
  while(num):
    remainder=num%10
    if(tmp % remainder ==0):
      return True
    num /= 10
  return False

print(divisibility_check(15))
print(divisibility_check(123))
print(divisibility_check(1511))
print(divisibility_check(143))


