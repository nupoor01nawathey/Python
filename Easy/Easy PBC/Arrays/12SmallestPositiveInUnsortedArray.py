# 12 Find the smallest positive number missing from an unsorted array
# Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.
# Note: You can modify the original array.

# Input:  arr[] = {2, 3, 7, 6, 8, -1, -10, 15}
# Output: 1

# Input:  arr[] = { 2, 3, -7, 6, 8, 1, -10, 15 }
# Output: 4

# Input: arr[] = {1, 1, 0, -1, -2}
# Output: 2

# Create a list full of 0’s with the size of the max value of the given array. 
# Now, whenever we encounter any positive value in the original array, change the index value of the list to 1. 
# After that simply iterate through the modified list, the first 0 encountered, (index value + 1) should be the answer.


def find_smallest_positive_mising_number_from_unsorted(A):
	m = max(A)
	if m < 1:
		return 1
	if len(A) == 1:
		return 2 if A[0] == 1 else 1
		
	l = [0] * m
	for i in range(len(A)):
		if A[i] > 0:
			if l[A[i] - 1] != 1:
				l[A[i] - 1] = 1
	for i in range(len(l)):
		if l[i] == 0:
			return i + 1
	return i + 2


print(find_smallest_positive_mising_number_from_unsorted([0, 10, 2, -10, -20])) # 1
print(find_smallest_positive_mising_number_from_unsorted([2, 3, 7, 6, 8, -1, -10, 15])) # 4
print(find_smallest_positive_mising_number_from_unsorted([2, 3, -7, 6, 8, 1, -10, 15])) # 2
print(find_smallest_positive_mising_number_from_unsorted([1, 1, 0, -1, -2])) # 2


# Time Complexity: O(N), Only two traversals are needed.
# Auxiliary Space: O(N), using the list will require extra space

