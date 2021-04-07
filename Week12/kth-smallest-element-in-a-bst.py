# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = 1
        self.smallest = None
        def inorder(node):
            if not node or self.smallest:
                return
            inorder(node.left)
            if self.counter == k:
                self.smallest = node.val
            self.counter += 1
            inorder(node.right)
        inorder(root)
        return self.smallest
