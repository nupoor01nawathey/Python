#4 One List Sort with Numerical Value | Accenture

l=['Sam200','Smith100','Zaid30','John50','Mayer99']

def sort_list_with_numerical_values(l):
  l1=[]
  for i in l:
    c=""
    for j in i:
      if j.isdigit():
        c=c+j
    l1.append(int(c))
    l1.sort()
  return l1
 
print(sort_list_with_numerical_values(l))


