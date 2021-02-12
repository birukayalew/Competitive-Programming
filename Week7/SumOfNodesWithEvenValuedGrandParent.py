# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        false_parent = 1
        if not root:
            return 
        return self.even_valued_grandparent(root,false_parent)
    def even_valued_grandparent(self,node,parent):
        total = 0
        if not node:
            return 0
        if node.left and parent % 2 == 0:
            total += node.left.val
        if node.right and parent % 2 == 0:
            total += node.right.val
            
        left = self.even_valued_grandparent(node.left,node.val)
        right = self.even_valued_grandparent(node.right,node.val)
        
        return left + right + total
        
