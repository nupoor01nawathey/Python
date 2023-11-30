#18 Find the unique words from the give input string

s="good morning good day good night"

def unique_words_1(s):    
  base_dict={}
  for i in s.split(" "):
    if i in base_dict:
      base_dict[i] += 1
    else:
      base_dict[i] = 1
  
  l=[k for k,v in base_dict.items() if v==1] # good appears more than once so not unique
  return l
  
print(unique_words_1(s))



from collections import Counter

def unique_words_2(num):    
  base_dict=Counter(s.split(" "))
  l=[k for k,v in base_dict.items() if v==1] # good appears more than once so not unique
  return l
  
print(unique_words_2(s))