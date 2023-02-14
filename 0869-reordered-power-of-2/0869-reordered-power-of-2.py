class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        basket = [2**i for i in range(0,36) if 2**i < 10**9]
        def sortNum (n):
            return "".join(sorted(str(n)))
        for i in range(len(basket)):
            basket[i] = sortNum(basket[i])
        return sortNum(n) in basket