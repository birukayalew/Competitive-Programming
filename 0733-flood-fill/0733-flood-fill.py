class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(image), len(image[0])
        original_color = image[sr][sc] 
        image[sr][sc] = color
        q = deque([(sr, sc)])
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < n and 0 <= new_j < m and image[new_i][new_j] != color and image[new_i][new_j] == original_color:
                    image[new_i][new_j] = color
                    q.append((new_i, new_j))
                    
        return image
                                