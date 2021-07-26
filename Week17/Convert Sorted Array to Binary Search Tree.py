# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left = 0
        right = len(nums) - 1
        
        return self.recursive(left,right,nums)
    
    def recursive(self,left,right,nums):
        if left > right:
            return None
        
        mid = (left + right) // 2
        curr_node = TreeNode(nums[mid])
        curr_node.left = self.recursive(left,mid - 1,nums)
        curr_node.right = self.recursive(mid + 1,right,nums)
        
        return curr_node
        
