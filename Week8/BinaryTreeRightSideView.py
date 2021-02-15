# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            ans.append(queue[-1].val)
            for i in range(length):
                poped = queue.popleft()
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
        return ans
                
                
        
