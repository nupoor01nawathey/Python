# Python Program for n-th Fibonacci number

# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

# Fn = Fn-1 + Fn-2
# With seed values 

# F0 = 0 and F1 = 1.

n=int(input())

def fibonacci_recursion(n):
  if n<=0:
    print("Incorrect input number")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
  
print(fibonacci_recursion(n))
# Time Complexity: O(2N)
# Auxiliary Space: O(N)




# creating an array in the function to find the
#nth number in fibonacci series. [0, 1, 1, ...]
def fibonacci_using_arrays(n):
	if n <= 0:
		return "Incorrect Output"
	data = [0, 1]
	if n > 2:
		for i in range(2, n):
			data.append(data[i-1] + data[i-2])
	return data[n-1]

# Driver Program
print(fibonacci_using_arrays(n))
