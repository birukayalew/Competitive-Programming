from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        ans = [[root.val]]
        temp = []
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                for child in curr.children:
                    temp.append(child.val)
                    q.append(child)
            ans.append(temp)
            temp = []
        ans.pop()
        return ans
            
            
            
