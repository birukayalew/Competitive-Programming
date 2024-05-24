class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == val:
                while i < j and nums[j] == val:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            
        for i in range(len(nums)):
            if nums[i] == val:
                return i
        return len(nums)