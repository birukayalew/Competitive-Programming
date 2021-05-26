# Based on Kadane's algorithm.
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        return max(self.helper(nums),self.helper([-1*x for x in nums]))
                   
    def helper(self,nums):
        best_max = -float('inf')
        curr_max = 0
        for i in range(len(nums)):
            curr_max += nums[i]
            if best_max < curr_max : best_max = curr_max
            if curr_max < 0 : curr_max = 0   
        return best_max
