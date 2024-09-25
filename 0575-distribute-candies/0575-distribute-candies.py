class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dc = set(candyType)
        n = len(candyType)
        if len(dc) >= n // 2:
            return n // 2
        return len(dc)