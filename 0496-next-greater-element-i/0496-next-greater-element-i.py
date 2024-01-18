class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}  # Dictionary to store next greater elements
        stack = []  # Monotonic stack (stores elements in descending order)

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater_map[stack.pop()] = num  # Update dictionary with next greater
            stack.append(num)

        while stack:
            next_greater_map[stack.pop()] = -1

        result = [next_greater_map[x] for x in nums1]  

        return result