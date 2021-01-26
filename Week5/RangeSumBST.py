# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans=[]
        self.show(root,ans)
        total=0
        for num in ans:
            if num>=low and num<=high:
                total+=num
        return total
    def show(self,root,ans):
        if root:
            self.show(root.left,ans)
            ans.append(root.val)
            self.show(root.right,ans)
            
            
            
               
