# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


# Solution 1 with lists fucntions
def searchInsert(nums: list[int], target: int) -> int:
    try: 
        return nums.index(target)
    except: 
        nums.append(target)
        nums.sort()
        return nums.index(target)

nums = [1, 3, 4, 5]
print(searchInsert(nums, 2))

# Solution 2 with Binary Search
def searchInsert(nums: list[int], target: int) -> int:
    length = len(nums)
    left = 0
    right = length 
    while (left < right):
        middle = (left + right) // 2
        if nums[middle] == target: 
            return middle
        elif nums[middle] < target: 
            left = middle + 1
        elif nums[middle] > target: 
            right -= 1
    return left
        
nums2 = [1, 2, 3, 4, 5, 6, 7]
print(searchInsert(nums2, 4))