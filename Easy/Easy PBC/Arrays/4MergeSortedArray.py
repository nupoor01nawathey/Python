# 4 Merge an array of size n into another array of size m+n
# Merge Sorted Array

# There are two sorted arrays. First one is of size m+n containing only m elements. 
# Another one is of size n and contains n elements. Merge these two arrays into the first array of size m+n such that the output is sorted. 
# Input: array with m+n elements (mPlusN[]). 

def merge_sorted_array(nums1, nums2):
  m=len(nums1)
  n=len(nums2)
  
  # get last index
  last=m+n-1
  
  # merge in reverse order
  while m >0 and n>0:
    if nums1[m-1] > nums2[n-1]:
      nums1[last] = nums1[m-1]
      m -= 1
    else:
      nums1[last] = nums2[n-1]
      n -= 1
    last -= 1
  
  # fill nums1 with leftover nums2 elements because we are inserting bigger nums in reverse order
  # there could be a case where nums2 last elements since smaller are not pushed to nums1
  # below will work only if there are elements left in nums2
  while n >0 :
    nums1[last] = nums2[n-1]
    n, last = n-1, last-1
  
  return nums1

print(merge_sorted_array([1,2,3], [2,5,6]))
print(merge_sorted_array([2,2,3], [1,5,6]))

# Time Complexity: O(n)
# Auxiliary Space: O(n)

