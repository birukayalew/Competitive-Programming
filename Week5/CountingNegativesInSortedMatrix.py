class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        subIndex=0
        mainIndex=len(grid)-1
        count=0
        while mainIndex>=0:
            if grid[mainIndex][subIndex]<0:
                count+=len(grid[mainIndex])-subIndex
                mainIndex-=1 
            else:
                subIndex+=1
                if subIndex>=len(grid[mainIndex]):
                    subIndex-=1
                    mainIndex-=1
        return count
                
