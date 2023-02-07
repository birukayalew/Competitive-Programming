import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        hp.heapify(nums)
        for i in range(k):
            poped = hp.heappop(nums)
        return -1*poped