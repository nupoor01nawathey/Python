# Python program to split array and move first part to end.

# Examples:

# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}

# Explanation : Split from index 2 and first 
# part {12, 10} add to the end .

# Input : arr[] = {3, 1, 2}
#           k = 1
# Output : arr[] = {1, 2, 3}
# Explanation : Split from index 1 and first
# part add to the end.

def splitArr(arr, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(len(arr)-1):
			arr[j] = arr[j + 1]

		arr[len(arr)-1] = x
	return arr

arr = [12, 10, 5, 6, 52, 36]
position = 2

print(splitArr(arr, position))

# Time complexity: O(nk), where n is the length of the array and k is the number of times the first part of the array needs to be moved to the end.
# Auxiliary space: O(1), the program only uses a constant amount of additional memory.


print("Using slicing approach",arr[:position]+arr[position:])


