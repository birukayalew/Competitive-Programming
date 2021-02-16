# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = deque()
        alternate = True
        ans = [[root.val]]
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                poped = queue.popleft()
                
                if poped.left:
                    queue.append(poped.left)
                if poped.right:
                    queue.append(poped.right)
            if alternate:
                temp = []
                for i in range(len(queue)-1,-1,-1):
                    temp.append(queue[i].val)
                alternate = False
            else:
                temp = []
                for i in range(len(queue)):
                    temp.append(queue[i].val)
                alternate = True
            ans.append(temp)
        ans.pop()
        return ans
                
