class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        index = 0
        number_of_provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                number_of_provinces += 1
                self.dfs(isConnected[i],visited,index,isConnected)

        return number_of_provinces
        
    def dfs(self,city_info,visited,index,isConnected):
        for i in range(len(city_info)):
            if city_info[i] == 1 and i not in visited: 
                visited.add(i)
                self.dfs(isConnected[i],visited,i,isConnected)
            
        
            
        
    
        
        
        
        
        
        
        
    
        






















                    
            
                    
        
