class Solution:
    def minOperations(self, n: int) -> int:
        target = (1 + (2 * (n-1) + 1)) // 2   #average
        ans = 0
        for index in range(n//2):
            ans += (target - ((2 * index) + 1))
        return ans
    
