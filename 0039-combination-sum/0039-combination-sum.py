class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def backtrack(current_sum, current_combination, start_index):
            if current_sum == target:
                result.append(current_combination.copy())  # Add a copy to avoid modifications
                return
            if current_sum > target:
                return 

            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                current_combination.append(candidate)
                backtrack(current_sum + candidate, current_combination, i)  
                current_combination.pop()  # Backtrack by removing the element

            
        
        backtrack(0, [], 0)
        return result
        