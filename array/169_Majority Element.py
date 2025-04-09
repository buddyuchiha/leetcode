# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
import time

# Solution 1 Boyer-Moore algorithm
def majorityElement(arr: list[int]) -> int:
    n = len(arr)
    start_time = time.time()
    candidate = -1
    votes = 0
    
    for i in range (n):
        if (votes == 0):
            candidate = arr[i]
            votes = 1
        else:
            if (arr[i] == candidate):
                votes += 1
            else:
                votes -= 1
    count = 0
    
    for i in range (n):
        if (arr[i] == candidate):
            count += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    if (count > n // 2):
        return candidate
    else:
        return -1
    
# Solution 2
def majorityElement2(arr: list[int]) -> int:
    n = len(arr)
    start_time = time.time()
    result_dict = {}
    
    for i in range (n):
        if result_dict.get(arr[i]):
            result_dict[arr[i]] += 1
        else:
            result_dict[arr[i]] = 1
    
    if max(result_dict.values()) > n // 2:
        print("--- %s seconds ---" % (time.time() - start_time))
        return max(result_dict, key = result_dict.get)
    else:
        print("--- %s seconds ---" % (time.time() - start_time))
        return -1


nums = [1, 2, 1, 1, 2]
print(majorityElement(nums))