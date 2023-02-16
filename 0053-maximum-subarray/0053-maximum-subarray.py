class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = best = nums[0]
        for i in range(1,len(nums)):
            curr = max(curr+nums[i],nums[i])
            best = max(curr,best)
        return best