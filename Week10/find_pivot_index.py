class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        suffix_sum = [nums[-1]]
        for i in range(1,len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
            suffix_sum.append(nums[len(nums)-1-i] + suffix_sum[i-1])
            
        suffix_sum.reverse()
        
        for i in range(len(prefix_sum)):
            if prefix_sum[i] == suffix_sum[i]:
                return i
        return -1
        
        
