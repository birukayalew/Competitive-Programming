class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        n2_len = len(nums2)

        # Find next greater elements for all elements in nums2
        for i in range(n2_len - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            next_greater[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        # Build the result array
        ans = []
        for x in nums1:
            j = nums2.index(x)
            ans.append(next_greater[nums2[j]])
        return ans