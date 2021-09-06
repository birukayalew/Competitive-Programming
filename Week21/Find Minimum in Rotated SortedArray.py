class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        while nums[start] > nums[-1]:
            start += 1
        return nums[start]
