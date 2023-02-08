class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        return nums[-1] if len(nums) <= 2 else nums[len(nums) - 3]