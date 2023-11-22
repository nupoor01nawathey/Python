# 1. Sum of n natural numbers

num=int(input("Enter your number: "))
total=0
for i in range(1, num+1): 
  total = total + i
print(total) # 15 if num=5
