class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        temp_col = 0
        temp_row = 0
        if r * c != row * col:
            return mat
        ans = [[] for x in range(r)]     
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[temp_row].append(mat[i][j])
                temp_col += 1
                if temp_col == c:
                    temp_col = 0
                    temp_row += 1
        return ans
                
                
