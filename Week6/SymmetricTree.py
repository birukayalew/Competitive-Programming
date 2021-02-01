# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.symmetric(root.left,root.right)
    def symmetric(self,left_root,right_root):
        if left_root is None and right_root is None:
            return True
        if left_root is None or right_root is None:
            return False
        if left_root.val != right_root.val:
            return False
        return self.symmetric(left_root.left,right_root.right) and self.symmetric(left_root.right,right_root.left)
