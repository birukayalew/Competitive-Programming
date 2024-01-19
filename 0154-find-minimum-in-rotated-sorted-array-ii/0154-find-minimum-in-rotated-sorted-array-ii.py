class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:  # Note: Use '<' instead of '<=' here
            mid = left + (right - left) // 2

            # Case 1: If nums[mid] > nums[right], minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1 

            # Case 2: If nums[mid] < nums[right], minimum could be in either half
            elif nums[mid] < nums[right]:
                right = mid  # Note: Inclusive of mid

            # Case 3: nums[mid] == nums[right] (potential duplicates)
            else:  
                # Cannot deterministically reduce search space -> linear check 
                right -= 1   

        return nums[left]