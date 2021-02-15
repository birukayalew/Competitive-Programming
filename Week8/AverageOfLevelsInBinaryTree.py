# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return
        ans = [root.val]
        queue = deque()
        queue.append(root)
        while queue:
            curr_sum = 0
            counter = 0
            length = len(queue)
            for i in range(length):
                poped = queue.popleft()
                if poped.left:
                    queue.append(poped.left)
                    curr_sum += poped.left.val
                    counter += 1
                if poped.right:
                    queue.append(poped.right)
                    curr_sum += poped.right.val
                    counter += 1
            if counter:
                ans.append(curr_sum/counter)
        return ans
