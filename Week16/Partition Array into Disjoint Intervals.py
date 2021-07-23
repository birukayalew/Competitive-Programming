class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = [nums[0]]
        min_so_far = [nums[-1]]
        length = len(nums)
        for i in range(length - 2,-1,-1):
            if nums[i] < min_so_far[length - i - 2]:
                min_so_far.append(nums[i])
            else:
                min_so_far.append(min_so_far[length - i - 2]) 
        for i in range(1,length):
            if max_so_far[i - 1] <= min_so_far[length - i - 1]:
                return i 
            if nums[i] > max_so_far[i-1]:
                max_so_far.append(nums[i])
            else:
                max_so_far.append(max_so_far[i-1])
        
        
            
                
            
       
