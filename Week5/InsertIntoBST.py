# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Iterative Way
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        prev=None
        r=root
        while root:
            if val>root.val:
                prev=root
                root=root.right
            else:
                prev=root
                root=root.left
        if prev is None:
            r=TreeNode(val)
        else:
            if val>prev.val:
                prev.right=TreeNode(val)
            else:
                prev.left=TreeNode(val)
        return r
#Recursive way
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.addNode(root,val)
        if not root:
            root=TreeNode(val)
        return root
    def addNode(self,root,val):
        if root:
            if val > root.val:
                if root.right is None:
                    root.right=TreeNode(val)
                    return
                else:
                    self.addNode(root.right,val)
            else:
                if root.left is None:
                    root.left=TreeNode(val)
                    return
                else:
                    self.addNode(root.left,val)
                
