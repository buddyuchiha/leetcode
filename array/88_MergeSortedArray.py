# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be 
# ignored. nums2 has a length of n.

# Solution 1 
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1_temp, nums2_temp = [], []
    i, j = 0, 0
    while i <= m - 1: 
        nums1_temp.append(nums1[i])
        i += 1
    nums1.clear()
    nums1 += nums1_temp
    while j <= n - 1:
        nums2_temp.append(nums2[j])
        j += 1
    nums1 += nums2_temp
    nums1.sort()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3 
nums2 = [2, 5, 6]
n = 3 
print(merge(nums1, m, nums2, n))

