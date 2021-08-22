class Solution:
    def fib(self, n: int) -> int:
        return (self.fib(n-1)+self.fib(n-2)) if n>1 else 0 if n==0 else 1 
        
        
        
#using memo
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        return self.recursion(n,memo)
    
    def recursion(self,n,memo):
        if n == 0: return 0
        if n == 1: return 1
        if n in memo: return memo[n]
        
        memo[n] = self.recursion(n - 2,memo) + self.recursion(n - 1,memo)
        
        return memo[n]
        
