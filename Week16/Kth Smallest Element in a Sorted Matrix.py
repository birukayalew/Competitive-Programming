import heapq as heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        temp = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ans.append(matrix[i][j])
        heap.heapify(ans)
        for i in range(k):
            temp = heap.heappop(ans)
        return temp
