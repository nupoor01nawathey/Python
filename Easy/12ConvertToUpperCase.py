#12 Convert First and Last letter of each Word to the Upper Case of Sentence in Python

s='hello world' # => HellO WorlD


def first_and_last_letter_to_upper_case(s):    
  words=s.split(" ")
  s1=[]
  for i in words:
    s1.append(i[0].upper() + i[1:-1] + i[-1].upper())
  return " ".join(s1)

print(first_and_last_letter_to_upper_case(s))


