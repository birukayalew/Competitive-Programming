# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.descendant(root,p,q)
    def descendant(self,root,p,q):
        
        if p.val>root.val and q.val>root.val:
            return self.descendant(root.right,p,q)
        if p.val<root.val and q.val<root.val:
            return self.descendant(root.left,p,q)
        return root
            
        
        
        
        
