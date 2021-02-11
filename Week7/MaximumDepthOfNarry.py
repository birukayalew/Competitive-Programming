"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        maximum_depth = 0
        for child in root.children:
            maximum_depth = max(maximum_depth,self.maxDepth(child))
        return maximum_depth + 1
        
        
