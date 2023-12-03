#3 Print elements in nested list in Python | TigerAnalytics

l=[1,2,3,['Sam', 'Smith'], 45, [432, 'Chris'], 43, 'Sam']

def nested_elements_from_list(l):
  l1=[]
  for i in l:
    if(isinstance(i, list)):
      l1.extend(i)
  return l1
  
print(nested_elements_from_list(l)) # ['Sam', 'Smith', 432, 'Chris']