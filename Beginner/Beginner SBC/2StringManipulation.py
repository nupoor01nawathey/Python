#2 Insert a string in the middle of a given string | TCS 
# 'City:Kolkata-WestBengal' => 'City:Kolkata-State:WestBengal'

s="City:Kolkata-WestBengal"
def manipulate_string_1(s):   
  return s.replace('-', '-State:')

print(manipulate_string_1(s))


def manipulate_string_2(s):
  index=s.find('WestBengal')
  return s[:index]+'State:'+s[index:]
  
print(manipulate_string_2(s))


