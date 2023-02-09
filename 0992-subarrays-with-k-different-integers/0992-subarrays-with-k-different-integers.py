class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        ans = dp = 0
        i = 0
        for j in range(len(nums)):
            count[nums[j]] += 1
            if len(count) < k:
                continue
            elif len(count) == k:
                dp = max(dp, 1)
            else:
                del count[nums[i]]
                i += 1
                dp = 1
            while count[nums[i]] != 1:
                dp += 1
                count[nums[i]] -= 1
                i += 1
            ans += dp
        return ans