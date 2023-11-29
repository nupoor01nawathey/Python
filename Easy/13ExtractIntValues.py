#13 FIND INTEGER VALUES FROM EACH ELEMENT WITHOUT USING LOOP


def extract_int_values(l):    
  l1=[int(i.split(" ")[0]) for i in l]
  return l1

print(extract_int_values(["30 student", "5 student", "7 student"])) # [30, 5, 7]


