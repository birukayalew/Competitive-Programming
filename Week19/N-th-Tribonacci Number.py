class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        return self.recursion(n,memo)
        
    def recursion(self,n,memo):
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        if n in memo: return memo[n]
        
        memo[n] = self.recursion(n - 3,memo) + self.recursion(n - 2,memo) + self.recursion(n - 1,memo)
        
        return memo[n]
