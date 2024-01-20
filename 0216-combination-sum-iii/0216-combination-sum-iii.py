class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(comb, remain, start_num):
            if remain == 0 and len(comb) == k:  # Condition: k numbers sum up to n
                res.append(list(comb))
                return

            elif remain < 0 or len(comb) == k:  # Exceeded target or exceeded number limit
                return

            for i in range(start_num, 10):  # Numbers from 1 to 9
                if i in comb:
                    continue
                    
                comb.append(i)
                backtrack(comb, remain - i, i + 1)
                comb.pop()
            
        res = []
        backtrack([], n, 1)
        return res