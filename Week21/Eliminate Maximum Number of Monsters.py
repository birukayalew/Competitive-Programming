import heapq as hp
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = []
        for i in range(len(speed)):
            ans.append(dist[i] / speed[i])
        hp.heapify(ans)
        curr = 0
        while ans:
            if hp.heappop(ans) <= curr:
                return curr
            curr += 1
        return curr
        
