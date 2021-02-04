import heapq as heap
import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*x for x in stones]
        heap.heapify(stones)
        print(stones)
        while len(stones)>1:
            heavy1 = heap.heappop(stones)*-1
            heavy2 = heap.heappop(stones)*-1
            if heavy1 != heavy2:
                heap.heappush(stones,int(-1*(math.fabs(heavy1-heavy2))))
        if len(stones)==0:
            return 0
        return heap.heappop(stones)*-1
