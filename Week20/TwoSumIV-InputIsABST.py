# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        return self.dfs(root,seen,k)
        
    def dfs(self,node,seen,target):
        if not node:
            return False
        
        if (target - node.val) in seen:
            return True
            
        seen.add(node.val)
        left = self.dfs(node.left,seen,target)
        right = self.dfs(node.right,seen,target)
        
        return left or right
        
