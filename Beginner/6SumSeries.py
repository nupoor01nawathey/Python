# 6. Sum series
# 1/1 + 2^2/2 + 3^3/3 + 4^4 / 4

n=int(input("Enter first number: " ))

# For finding sum from 1/2 till 3^3/3
# 1/1 + 2*2/2 + 3*3*3/3 => 1 + 2 + 9 => 12
# n=4 
total=0
for i in range(1, 4):
  a=float(i**i)/i
  total=total+a
print(total)