class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        length = len(edges)
        visited = set()
        for i in range(length):
            parent = edges[i][0]
            child = edges[i][1]
            graph[parent].append(child)
            graph[child].append(parent)
        return self.dfs(0,graph,hasApple,visited)
            
    def dfs(self,node,graph,hasApple,visited):
        if node in visited:
            if hasApple[node]:
                return 2
            return 0
        visited.add(node)
        time = 0
        for neighbour in graph[node]:
            if neighbour not in visited:
                time += self.dfs(neighbour,graph,hasApple,visited)
        if (hasApple[node] or time != 0) and node != 0:
            return time + 2
        return time
