class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = float('inf')
        profit = 0
        for price in prices:
            profit = max(profit, price - curr)
            curr = min(curr, price)
            
        return profit