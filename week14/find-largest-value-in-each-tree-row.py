# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        answer = [root.val]
        while queue:
            length = len(queue)
            maximum = -float('inf')
            for i in range(length):
                parent = queue.popleft()
                if parent.left:
                    queue.append(parent.left)
                    maximum = max(maximum,parent.left.val)
                if parent.right:
                    queue.append(parent.right)
                    maximum = max(maximum,parent.right.val)
            answer.append(maximum)
        answer.pop()
        return answer
        
