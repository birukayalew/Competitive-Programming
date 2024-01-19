class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Case 1: Array is not rotated, minimum is at the start
            if nums[low] <= nums[high]:
                return nums[low]

            # Case 2: Mid element is the minimum
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Case 3: Minimum lies on the right side
            if nums[mid] > nums[high]:
                low = mid + 1
            # Case 4: Minimum lies on the left side
            else:
                high = mid - 1

        return -1