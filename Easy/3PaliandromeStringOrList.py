#3 CHECK IF A STRING/LIST IS PALINDROME OR NOT

s=input("Enter a string: ")

def is_string_paliandrome(s):
  if(s.lower()==s[::-1].lower()):
    return True
  else:
    return False
    
print(is_string_paliandrome(s)) # True for wow, radar and False for lion, tiger



def is_list_paliandrome(l):
  for i in range(len(l) // 2):
    if l[i] != l[len(l) - i -1]:
      return False
  return True

print(is_list_paliandrome([1,2,3,2,1])) # True
print(is_list_paliandrome([1,2,2,1]))   # False
print(is_list_paliandrome([1,2,3,4,1])) # True
