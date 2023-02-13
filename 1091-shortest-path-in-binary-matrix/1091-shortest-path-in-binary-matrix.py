class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # instantiate the directions
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1,-1)]
        heap = []
        visited = set()
        if grid[0][0] == 0:
            # move, i, j
            heappush(heap, ((1, 0, 0)))
                     
        
        while heap:
            move, i, j = heappop(heap)
            
            if (i, j) == (n - 1, n - 1):
                return move
            
            if (i, j) not in visited:
                visited.add((i, j))
                for d in directions:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    
                    if 0 <= new_i < n and 0 <= new_j < n and (new_i, new_j) not in visited and grid[new_i][new_j] == 0:
                        heappush(heap, (move + 1, new_i, new_j))
                        
        return -1