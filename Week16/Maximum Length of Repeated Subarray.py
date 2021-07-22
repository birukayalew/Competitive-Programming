from collections import defaultdict
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = defaultdict(lambda:0)
        maximum = -float('inf')
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[(i,j)] = dp[(i-1,j-1)] + 1
                else:
                    dp[(i,j)] = 0
                maximum = max(maximum,dp[(i,j)])
        return maximum
