import heapq as heap
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = []
        final = []
        for i in range(len(arr)):
            heap.heappush(output,[abs(x - arr[i]),i])
        for i in range(k):
            final.append(arr[heap.heappop(output)[1]])
        final.sort()
        return final
            
