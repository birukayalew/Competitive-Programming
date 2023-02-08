class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        ans = []
        connected = defaultdict(set)
        
        for x, y in equations:
            connected[x].add(y)
            connected[y].add(x)
                
        def check(x, y, v):
            
            if x == y:
                return True
            val = False
            for item in connected[x]:
                if item not in v:
                    v.add(item)
                    val = val or check(item, y, v)
            return val
                
            
        for i, (x, y) in enumerate(equations):
            graph[x].append([y,values[i]])
            graph[y].append([x, 1 / values[i]])
            
        for q1, q2 in queries:
            v = set([(q1)])
            if (q2 not in connected or  q1 not in connected) or not check(q1, q2, v):
                ans.append(-1)
                continue
            visited = set()
            q = deque([(q1, 1)])
            while q:
                curr, cost = q.popleft()
                if curr == q2:
                    ans.append(cost)
                    break
                
                for item in graph[curr]:
                    if item[0] not in visited:
                        visited.add((item[0]))
                        q.append((item[0], cost * item[1]))
   
        return ans