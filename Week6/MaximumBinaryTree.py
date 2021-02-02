# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.maximum(nums)
    def maximum(self,nums):
        if len(nums) == 0:
            return
        root = TreeNode(max(nums))
        index = nums.index(root.val)
        root.left = self.maximum(nums[:index])
        root.right = self.maximum(nums[index+1:])
        return root
        
