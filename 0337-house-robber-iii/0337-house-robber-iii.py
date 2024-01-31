# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            # Base case: empty node
            if not node:
                return (0, 0)  # rob: 0, not_rob: 0

            left = helper(node.left)
            right = helper(node.right)

            # If you rob the current node
            rob = node.val + left[1] + right[1]  
            # If you don't rob the current node
            not_rob = max(left) + max(right)     

            return (rob, not_rob)
        
        
        return max(helper(root))

      
