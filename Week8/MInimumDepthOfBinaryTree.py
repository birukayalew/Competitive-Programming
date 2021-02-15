# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def leaf_node(self,node):
        return node.left == None and node.right == None
    
    # using dfs
    
    
    def minDepth(self,root: TreeNode) -> int:
        return self.min_depth_finder(root) 
    
    def min_depth_finder(self,root):
        if not root:
            return 0
        if self.leaf_node(root):
            return 1
        left = self.min_depth_finder(root.left) 
        right = self.min_depth_finder(root.right)
        
        if left == 0:
            return right + 1
        if right == 0:
            return left + 1
            
        return min(left,right) + 1 
        
        
        
        
    # using bfs
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        level = 1
        queue.append(root)
        while (queue):
            size = len(queue)
            for i in range(size):
                poped = queue.popleft()
                if (self.leaf_node(poped)):
                    return level
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
            level += 1
            
        return level
    
    
        
