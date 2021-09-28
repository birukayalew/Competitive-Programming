class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        ans = []
        while start <= end :
            if abs(nums[end]) > abs(nums[start]):
                ans.append(nums[end] ** 2)
                end -= 1
            else:
                ans.append(nums[start] ** 2)
                start += 1
        ans.reverse()
        return ans
