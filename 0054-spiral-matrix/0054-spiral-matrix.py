class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        
        while t <= b and l <= r:
            # top left to top right
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            
            t += 1
                
            # top right to bototm right
            for i in range(t, b + 1):
                ans.append(matrix[i][r])
            r -= 1
                
            # bottom right to bottom left
            for i in range(r, l - 1, -1):
                ans.append(matrix[b][i])
            b -= 1
                
            # bottom left to top left
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
            
        return ans[:len(matrix) * len(matrix[0])]