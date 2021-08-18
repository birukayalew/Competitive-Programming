from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        good_nodes = 1
        q.append((root,root.val))
        while q:
            curr_node,curr_max = q.popleft()
            if curr_node.left:
                curr_val = curr_node.left.val
                if curr_val >= curr_max:
                    good_nodes += 1
                q.append((curr_node.left,max(curr_val,curr_max)))
                
            if curr_node.right:
                curr_val = curr_node.right.val
                if curr_val >= curr_max:
                    good_nodes += 1
                q.append((curr_node.right,max(curr_val,curr_max)))
                
        return good_nodes
