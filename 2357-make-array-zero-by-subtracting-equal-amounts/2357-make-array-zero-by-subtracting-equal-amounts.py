class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        curr, ans = 0, 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]:
                diff = nums[i] - curr 
                if diff > 0:
                    curr += diff
                    ans += 1
        return ans
    