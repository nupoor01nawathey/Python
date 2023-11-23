# 7. Paliandrome String

s=String(input("Enter a string: " ))

# s="malyalam"  # not a paliandrome
# s="wow"       # paliandrome

s=s.casefold() # To lowercase

reversedS = s[::-1]  # OR reversedS=reversed(s)

if(list(s) == list(reversedS)):
  print("paliandrome")
else:
  print("not a paliandrome")