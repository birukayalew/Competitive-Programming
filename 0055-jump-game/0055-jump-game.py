class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        curr_step = nums[0]
        for i in range(1, len(nums) - 1):
            if curr_step == 0:
                return False
            if nums[i] >= curr_step:
                curr_step = nums[i]
            else:
                curr_step -= 1
        return True if curr_step != 0 else False
        
    
    
        