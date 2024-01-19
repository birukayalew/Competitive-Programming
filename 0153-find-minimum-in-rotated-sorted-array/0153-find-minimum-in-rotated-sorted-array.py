class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:  # Handle empty array
            return None  

        left = 0
        right = len(nums) - 1

        # Base case: If already sorted (no rotation)
        if nums[left] <= nums[right]:  
            return nums[left] 

        while left <= right:
            mid = left + (right - left) // 2

            # Check if mid itself is the minimum element
            if nums[mid] > nums[mid + 1]:  
                return nums[mid + 1]

            # Check if mid is in the right sorted portion (unrotated part)
            if nums[mid] < nums[left]: 
                # Minimum lies in the left half 
                right = mid - 1

            else:  # Mid lies in the left sorted portion
                # Minimum lies in the right half 
                left = mid + 1

        return None 