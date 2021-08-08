# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        ans = []
        self.dfs(root,[],ans,targetSum)
        return ans
    
    def dfs(self,node,temp,ans,curr_diff):
        
        if not node:
            return
        
        if self.check_leaf(node):
            if curr_diff == node.val:
                ans.append(temp + [node.val])
        
        self.dfs(node.left,temp + [node.val],ans,curr_diff - node.val)
        self.dfs(node.right,temp + [node.val],ans,curr_diff - node.val)

        
        return ans 
    
    def check_leaf(self,node):
        if not (node.left or node.right):
            return True
        return False
        
