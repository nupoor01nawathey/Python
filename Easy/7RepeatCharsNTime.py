#7 Repeat Char in a string N times


def n_times_char_1(s, n):
  s1=""
  for i in s:
    s1 = s1 + i * n
  return s1

print(n_times_char_1('Hello',3))
print(n_times_char_1('',3))




def n_times_char_2(s, n):
  if len(s) == 0:
    return ""
  return s[0]*n + n_times_char_2(s[1:] ,n)

print(n_times_char_2('Hello',3))
print(n_times_char_2('010',3))
