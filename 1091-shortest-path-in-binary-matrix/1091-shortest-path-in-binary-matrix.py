class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1,-1)]
        visited = set([(0, 0)])
        q = deque([(1, 0, 0)])
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        while q:
            move, i, j = q.popleft()
            if (i, j) == (n-1, n-1):
                return move
            
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                    visited.add((new_i, new_j))
                    q.append((move + 1, new_i, new_j))
        return -1        