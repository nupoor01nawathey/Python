# 4. Swap two numbers using reference variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# a=10
# b=20
# 1. Use a temporary variable to store 1st value and keep rotating value as below
tmp=a
a=b
b=tmp

print(a,b)


# a=10
# b=20
# 2. a=a+b then b=a-b then a=a-b
a=a+b # 10+20=30
b=a-b # 30-20=10
a=a-b # 30-10=20

print(a,b)
