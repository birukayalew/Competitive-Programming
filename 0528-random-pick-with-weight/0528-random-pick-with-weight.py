class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.cumsum = list(accumulate(w))

    def pickIndex(self) -> int:
        pick = randint(1, self.total)
        index = bisect_left(self.cumsum, pick)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
        