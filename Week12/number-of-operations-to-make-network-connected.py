class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        leader = [x for x in range(n)]
        size = [ 1 for x in range(n)]
        visited = set()
        extra_cables = 0
        excluded_comps = 0
        def find(comp):
            if comp == leader[comp]:
                return comp
            leader[comp] = find(leader[comp])
            return leader[comp]
        
        def union(comp1,comp2):
            comp1_leader = find(comp1)
            comp2_leader = find(comp2)
            if leader[comp1_leader] > leader[comp2_leader]:
                leader[comp2_leader] = comp1_leader
            else:
                leader[comp1_leader] = comp2_leader
                
        for x,y in connections:
            if x not in visited:
                visited.add(x)
            if y not in visited:
                visited.add(y)
            x_leader = find(x)
            y_leader = find(y)
            if x_leader == y_leader:
                extra_cables += 1
            else:
                union(x,y)
        for i in range(len(leader)):
            if leader[i] == i:
                excluded_comps += 1
        return excluded_comps - 1 if extra_cables >= excluded_comps - 1 else -1
            
        
        
        
        
        
    
    
    
