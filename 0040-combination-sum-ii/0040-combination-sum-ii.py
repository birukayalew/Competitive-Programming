class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(comb, remain, curr_index):
            if remain == 0:
                res.append(list(comb))  
                return
            elif remain < 0 or curr_index == len(candidates):
                return

            # Track used elements to avoid duplicates
            used = set()
            
            for i in range(curr_index, len(candidates)):
                if candidates[i] not in used and remain - candidates[i] >= 0:
                    used.add(candidates[i])
                    comb.append(candidates[i])
                    backtrack(comb, remain - candidates[i], i + 1)  # Move to the next candidate
                    comb.pop()
                    
        res = []
        candidates.sort()  # Sorting can help in pruning branches early
        backtrack([], target, 0)
        return res


            