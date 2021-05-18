class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        maximum = -1
        for i in range(len(arr)):
            maximum = max(maximum,arr[i])
            if i == maximum : chunks += 1
        return chunks
            
