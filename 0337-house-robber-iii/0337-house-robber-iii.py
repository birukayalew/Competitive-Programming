# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def rob_tree_helper(root):
            # Returns a tuple (rob_root, not_rob_root)
            # rob_root: maximum money if this root is robbed
            # not_rob_root: maximum money if this root is not robbed

            if not root:
                return (0, 0)

            left = rob_tree_helper(root.left)
            right = rob_tree_helper(root.right)

            # If we rob this root, we cannot rob its children
            rob_root = root.val + left[1] + right[1]

            # If we don't rob this root, we can choose whether to rob its children
            not_rob_root = max(left) + max(right)

            return (rob_root, not_rob_root)
        
        result = rob_tree_helper(root)
        return max(result)

      
