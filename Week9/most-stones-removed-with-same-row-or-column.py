class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        graph = defaultdict(list) #connected coordinates
        visited = set()
        stack = [] #where we are currently
        group = 0 #number of groups so far
        
        
        for i in range(len(stones)):
            for j in range(len(stones)):
                if i != j:
                    
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]: #on same row or column
                        graph[tuple(stones[i])].append(tuple(stones[j]))
                        
        for i in range(len(stones)):
            
            curr_stone = tuple(stones[i])
            if curr_stone not in visited:
                group += 1
                visited.add(curr_stone)
                stack.append(curr_stone)
                
                while stack:
                    curr = stack.pop()
                    for neighbours in graph[curr]:
                        if neighbours not in visited:
                            visited.add(neighbours)
                            stack.append(neighbours)
                            
        return len(stones)-group
        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
