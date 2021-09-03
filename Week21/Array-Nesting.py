class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_move = float('-inf')
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                max_move = max(max_move,self.dfs(nums[i],visited,nums,i))
        return max_move
                
    def dfs(self,curr,visited,nums,index):
        res = 0
        if index == curr:
            return 1
        
        if curr not in visited:
            visited.add(curr)
            res = self.dfs(nums[curr],visited,nums,index) + 1
            
        return res
        
                
            
            
            
