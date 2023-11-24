# 9. Conversion of lowercase to uppercase using chr , ord

s=input("Enter a string: " )

# s="hii" => HII
new=""
for i in s:
  new=new+chr(ord(i)-32)
print(new, end="")


