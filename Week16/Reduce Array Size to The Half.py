from collections import Counter
import heapq as heap
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) / 2
        arr = Counter(arr)
        ans = []
        minimum = 0
        curr_sum = 0
        for key in arr:
            heap.heappush(ans,-1 * arr[key])
        while curr_sum < half:
            minimum += 1
            curr_sum += -1 * heap.heappop(ans)
        return minimum
