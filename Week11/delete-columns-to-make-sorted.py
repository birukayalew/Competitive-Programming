class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        column = 0
        for i in range(len(strs[0])):
            for j in range(len(strs) - 1):
                if strs[j + 1][i] < strs[j][i]:
                    column += 1
                    break
        return column
                    
            
            
                
