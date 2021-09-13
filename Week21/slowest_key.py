class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        d = {}
        d['max'] = [keysPressed[0],releaseTimes[0]] 
        for i in range(1,len(keysPressed)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            if diff > d['max'][1]:
                d['max'] = [keysPressed[i],diff] 
            elif diff == d['max'][1]:
                if keysPressed[i] > d['max'][0]:
                    d['max'] = [keysPressed[i],diff] 
                        
        return d['max'][0]
                        

                    
