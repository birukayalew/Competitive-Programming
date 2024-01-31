class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)

        def helper(nums):  # Helper function for linear house robbing
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[-1]

        # Case 1: Rob the first house, not the last
        case1 = helper(nums[:-1])
        # Case 2: Don't rob the first, potentially rob the last
        case2 = helper(nums[1:])

        return max(case1, case2)