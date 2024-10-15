class Solution:
    def jump(self, nums: List[int]) -> int:
        
        @cache
        def helper(index):
            if index == len(nums) - 1:
                return 0
            
            if index >= len(nums):
                return float('inf')
            
            res = float('inf')
            
            for next_idx in range(1, nums[index] + 1):
                res = min(res, 1 + helper(index + next_idx))
            
            return res
        
        return helper(0)