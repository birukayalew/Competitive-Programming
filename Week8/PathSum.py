# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf_node(self,root):
        return root.left == None and root.right == None
    
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        return self.checker(root,targetSum)
    
    
    def checker(self,node,targetSum):
        
        if not node:
            return False
        
        if(node.val == targetSum and self.leaf_node(node)):
            return True
        
        left = self.checker(node.left,targetSum-node.val)
        right = self.checker(node.right,targetSum-node.val)
        
        return left or right
        
        
        
        
        
        
        
#        
