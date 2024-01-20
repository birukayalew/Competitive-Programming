class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(comb, remain, start):
            if remain == 0 and len(comb) == k:
                res.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return

            for i in range(start, 10):  # Use numbers from 1 to 9
                comb.append(i)
                backtrack(comb, remain - i, i + 1)  # Next number must be larger than i
                comb.pop()
            
        res = []
        backtrack([], n, 1)
        return res