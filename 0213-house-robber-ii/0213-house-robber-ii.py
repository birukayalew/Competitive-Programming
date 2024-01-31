class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def rob_linear(nums):
        
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

            return dp[-1]
        
        
        if not nums:
            return 0
        if len(nums) == 1:  # Special case: only one house
            return nums[0]

        # Case 1: Robbing the first house (exclude the last)
        max1 = rob_linear(nums[:-1])

        # Case 2: Not robbing the first house (can rob the last)
        max2 = rob_linear(nums[1:]) 

        return max(max1, max2)