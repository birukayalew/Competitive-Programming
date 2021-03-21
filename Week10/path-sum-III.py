# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> int:
        
        if not root:
            return 0
        prefix_sum = defaultdict(lambda:0)         #to store running sum
        prefix_sum[0] += 1         # incase root is equal to target sum 
        
        return self.dfs(root,0,target_sum,prefix_sum)
    
    def dfs(self,node,current_sum,target_sum,prefix_sum):
        count = 0       # number of paths that sum to target value
        if not node:
            return 0
        
        current_sum += node.val    #running sum
        if current_sum - target_sum in prefix_sum:      #if its complement is found
            count += prefix_sum[current_sum - target_sum]
        prefix_sum[current_sum] += 1
        
        count += self.dfs(node.left,current_sum,target_sum,prefix_sum) + self.dfs(node.right,current_sum,target_sum,prefix_sum)    #apply for left and right childs
        
        prefix_sum[current_sum] -= 1 #backtracking the current sum
        
        return count
