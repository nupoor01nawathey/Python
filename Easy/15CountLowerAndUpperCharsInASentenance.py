#15 Count Lower and Upper case letters in a sentence 

s="Hello Good Morning Lisa, nice to meet You, 123"
def count_upper_and_lower_chars(s):
  cnt_upper, cnt_lower=0, 0
  for i in s:
    if (i.islower()):
      cnt_lower+=1
    if (i.isupper()):
      cnt_upper+=1
  return cnt_lower, cnt_upper

print(count_upper_and_lower_chars(s))
