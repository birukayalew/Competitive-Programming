class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(math.sqrt(c))
        while start <= end:
            curr = start**2 + end**2 
            if curr == c:
                return True
            if curr < c: 
                start += 1
            else:
                end -= 1
                
        return False
