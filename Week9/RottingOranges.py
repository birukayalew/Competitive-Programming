class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        
        col = len(grid[0])
        
        minute = 0
        
        rotten_oranges = []
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    rotten_oranges.append((i,j))
        
        
        
        def fresh_to_rotten(rotten_oranges):
            freshes = []
            directions = [0,1,0,-1,0]
            for pos in range(len(directions)-1):
                
                for rotten_pos in rotten_oranges:
                    
                    new_i = rotten_pos[0] + directions[pos]
                    new_j = rotten_pos[1] + directions[pos + 1]
                  
                
                    
                    if 0 <= new_i < row and 0 <= new_j < col and grid[new_i][new_j] == 1:
                        freshes.append((new_i,new_j))
                        grid[new_i][new_j] = 2
            return freshes
            
        
        
                    
        while rotten_oranges:
            
            rotten_oranges = fresh_to_rotten(rotten_oranges)
            
            if len(rotten_oranges) == 0:
                break
                
            minute += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return minute
            
