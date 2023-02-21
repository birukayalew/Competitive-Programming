class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0 for x in range(n)]
        ans = []
        for x,y in edges:
            indegree[y] += 1
        for i,val in enumerate(indegree):
            if val == 0:
                ans.append(i)
        return ans