class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = 1
        answer = [1]
        for i in range(len(nums)-1):
            answer.append(nums[i] * answer[-1])
        for i in range(len(nums) - 1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
            
            
        
