class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            
        @cache
        def dfs(c):
            res = True
            visited.add(c)
            for neighbour in graph[c]:
                if neighbour in visited:
                    return False
                res = res and dfs(neighbour)
            visited.remove(c)
            return res
        
        for c in range(numCourses):
            res = dfs(c)
            if not res:
                return False
            
        return True