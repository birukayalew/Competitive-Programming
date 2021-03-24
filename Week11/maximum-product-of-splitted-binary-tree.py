# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        max_product = [0]
        total_sum = self.total_sum_finder(root)
        self.product_helper(root,total_sum,max_product)
        return max_product[0] % (10**9 + 7)
     
    def total_sum_finder(self,node):
        if not node:
            return 0
        return self.total_sum_finder(node.left) + self.total_sum_finder(node.right) + node.val
    
    def product_helper(self,node,total_sum,max_product):
        if not node:
            return 0
        left = self.product_helper(node.left,total_sum,max_product)
        right = self.product_helper(node.right,total_sum,max_product)
        if (node.right):
            rest = total_sum - right
            product = rest * right
            max_product[0] = max(max_product[0],product)
        if (node.left):
            rest = total_sum - left
            product = rest * left
            max_product[0] = max(max_product[0],product)
        
        return node.val + left + right 
        
            
            
