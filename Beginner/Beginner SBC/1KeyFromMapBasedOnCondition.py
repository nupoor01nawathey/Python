#1 Find the key from Map with K, V pair where V is greater than 100 | Tiger Analytics

base_map = {
  'a': 150,
  'b': 75,
  'c': 200,
  'd': 50,
  'e': 300
  
}

def find_key_from_map_based_on_condition_1(base_map, n):   
  l=[]
  for k,v in base_map.items():
    if v > n:
      l.append(k)
  return l

print(find_key_from_map_based_on_condition_1(base_map, 100))




def find_key_from_map_based_on_condition_2(base_map, n):   
  return [k for k,v in base_map.items() if v > n]

print(find_key_from_map_based_on_condition_2(base_map, 100))


