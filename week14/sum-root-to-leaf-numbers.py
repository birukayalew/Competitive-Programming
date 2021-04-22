# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        answer = 0
        return self.dfs(root,answer)
        
    def dfs(self,node,answer):
        if not node:
            return 0
        answer *= 10
        answer += node.val
        if self.leaf(node):
            return answer
        left = self.dfs(node.left,answer)
        right = self.dfs(node.right,answer)
        return left + right
        
    def leaf(self,node):
        return not(node.left or node.right)
