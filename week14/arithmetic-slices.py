class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        diff = []
        start = 0
        end = 1
        slices = 0
        for i in range(len(nums) - 1):
            curr = nums[i + 1] - nums[i]
            diff.append(curr)
        while end < len(diff):
            if diff[start] == diff[end]:
                possible_middle_slices = end - start -1
                slices += (1 + possible_middle_slices)
            else:
                start = end
            end += 1
        return slices
            
