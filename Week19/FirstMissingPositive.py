#O(n) space and O(n) time complexity

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minimum = 1
        length = len(nums)
        sort = [0 for x in range(length)]
        
        
        for i in range(length):
            if nums[i] >= 1 and nums[i] <= length:
                sort[nums[i] - 1] = nums[i]
        for i in range(length):
            if sort[i] >= 1:
                if sort[i] == minimum:
                    minimum += 1
                else:
                    return minimum
        return minimum

#O(1) space and O(n) time complexity

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            curr = nums[i]
            nums[i] = 0
            while 1 <= curr <= length and curr != nums[curr - 1]:
                temp2 = nums[curr - 1]
                nums[curr - 1] = curr
                curr = temp2
        
        for i in range(length):
            if nums[i] == 0:
                return i + 1
        return length + 1
                    
            

                
        
        


    
