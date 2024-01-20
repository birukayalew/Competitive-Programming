class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True  # Duplicate found within k distance

            seen.add(nums[i])

            if len(seen) > k:
                seen.remove(nums[i - k])  # Remove element to keep window size at k

        return False