class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.recursion(0,n,memo)
    def recursion(self,value,n,memo):
        if value == n:
            return 1
        if value > n:
            return 0
        if value in memo:
            return memo[value]
        
        memo[value] = self.recursion(value + 1,n,memo) + self.recursion(value + 2,n,memo)
        
        return memo[value]
