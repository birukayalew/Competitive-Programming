class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        visited = set()
        visited.add((sr,sc))
        rows = len(image)
        columns = len(image[0])
        
        self.dfs(image,sr,sc,visited,rows,columns,newColor,originalColor)
        return image
        
    def dfs(self,image,sr,sc,visited,rows,columns,newColor,originalColor):
        image[sr][sc] = newColor
        directions = [0,1,0,-1,0]
        for i in range(len(directions)-1):
            new_i = sr + directions[i]
            new_j = sc + directions[i+1]
            if(0 <= new_i < rows and 0 <= new_j < columns and image[new_i][new_j] == originalColor ):
                next_state = (new_i,new_j)
                if next_state not in visited:
                    visited.add(next_state)
                    self.dfs(image,new_i,new_j,visited,rows,columns,newColor,originalColor)
        
