#8 Reverse words in a sentenance
# Hello Steve, good morning => morning good Steve, Hello

def reverse_words_1(s):
  return(' '.join(s.split(" ")[::-1]))

print(reverse_words_1("Hello Steve, good morning"))



def reverse_words_2(s):
  words=s.split(" ")
  for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")
    
reverse_words_2("Hello Steve, good morning")


def reverse_words_3(s):
  print("\n\n")
  words=s.split(" ")
  w1=[]
  for i in range(len(words)-1, -1, -1):
    w1.append(words[i])
    a=' '.join(w1)    
  return a  
  
print(reverse_words_3("Hello Steve, good morning"))