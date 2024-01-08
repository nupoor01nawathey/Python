# GOAT problem
# Two Sum , return index of two numbers where two number sum equals given target

def two_sum(a, target):
  hash_map=dict()
  n = len(a)
  for i,x in enumerate(a):
    if x in hash_map:
      return hash_map[x], i
    else:
      hash_map[target-x]=i
  return [-1,-1]
  
print(two_sum((2,7,11,15), 9))


# Time complexity O(N) -> 1 iteration for iterating over the array a
# Space complexity O(N) -> No extra space is required