class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0 for i in nums]
        left = 0
        right = len(nums) - 1
        for pos in reversed(range(len(ans))):
            if abs(nums[left]) > abs(nums[right]):
                sq = nums[left] * nums[left]
                ans[pos] = sq
                left += 1
            else:
                sq = nums[right] * nums[right]
                ans[pos] = sq
                right -= 1
        return ans