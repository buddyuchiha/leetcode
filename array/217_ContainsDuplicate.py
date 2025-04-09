# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums: list[int]) -> bool:
    nums_2 = list(set(nums))
    return len(nums_2) > len(nums)

