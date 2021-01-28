class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while left<=right:
            if nums[mid]==target:
                return mid
            
            elif target>nums[mid]:
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        return -1
