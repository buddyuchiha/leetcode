# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> optional[TreeNode]:
        Nodes = []
        left = 0 
        right = len(nums) 
        while left <= right:
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            for i in range(middle):
                middle_left = (left + middle) // 2

            