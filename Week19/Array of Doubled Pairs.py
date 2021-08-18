from collections import defaultdict
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d = defaultdict(lambda : 0)
        for num in arr:
            d[num] += 1
            
        arr.sort(key=abs)
        
        for num in arr:
            if d[num] != 0:
                if d[2* num] == 0:
                    return False
                d[num] -= 1
                d[2 * num] -= 1
                
        return True 
    
    
