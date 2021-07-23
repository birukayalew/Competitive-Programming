# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not self.dfs(root):
            root = None
        return root
    
    def dfs(self,node):
        if not node:
            return False
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if not left:
            node.left = None
        if not right:
            node.right = None
        
        return node.val == 1 or left or right
        
