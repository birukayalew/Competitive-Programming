class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ans = []
        rotate = k % len(nums)
        for i in range(len(nums) - rotate,len(nums)):
            ans.append(nums[i])
        for i in range(len(nums) - rotate):
            ans.append(nums[i])
        for i in range(len(ans)):
            nums[i] = ans[i]
            
            
 #using two pointers
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length 
        self.reverse(nums,length - k,length - 1)
        self.reverse(nums,0,length - k - 1)
        self.reverse(nums,0,length - 1)
        
    def reverse(self,nums,left,right):
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
