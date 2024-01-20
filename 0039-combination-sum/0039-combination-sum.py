class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        def backtrack(comb, remain, curr_index):
            if remain == 0:
                # Found a valid combination, add it to the result
                res.append(list(comb))
                return
            elif remain < 0:
                # Exceeded the target, no need to explore further
                return
            for i in range(curr_index, len(candidates)):
            # Add the current candidate
                comb.append(candidates[i])

                # Recursively explore with the remaining target,
                # allowing the same candidate to be chosen again
                backtrack(comb, remain - candidates[i], i)

                # Backtrack: remove the candidate for other possibilities
                comb.pop()
            
        res = []
        backtrack([], target, 0)
        return res
        