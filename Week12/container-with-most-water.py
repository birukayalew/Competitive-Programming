class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left , right = 0, len(height) - 1
        for width in range(len(height) - 1,-1,-1):
            length = min(height[left],height[right])
            area = max(area,width * length)
            if length == height[left]:
                left += 1
            else:
                right -= 1
        return area
