# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq as hp
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # col,level,val
        heap = []
        # node,row,col,level
        q = deque([(root,0,0,0)])
        ans = []
        while q:
            l = len(q)
            for i in range(l):
                node,row,col,level = q.popleft()
                hp.heappush(heap,(col,level,node.val))
                if node.left:
                    q.append((node.left,row + 1, col - 1,level + 1))
                if node.right:
                    q.append((node.right,row + 1, col + 1, level + 1))
    
        
        last,level,curr = hp.heappop(heap)
        temp = [curr]
        while heap:
            col,level,curr = hp.heappop(heap)
            if last != col:
                ans.append(temp)
                temp = []
                last = col
            temp.append(curr)
                
        if temp:
            ans.append(temp)
        return ans