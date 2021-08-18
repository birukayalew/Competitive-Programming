class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        d = Counter(t)
        start = 0
        end = 0
        temp = defaultdict(lambda : 0)
        counter = 0
        min_length = float('inf')
        ans = [0,0]
        found = False
        
        while end < len(s):
            if s[end] in d:
                temp[s[end]] += 1
                if temp[s[end]] == d[s[end]]:
                    counter += 1
                
            if counter == len(d):
                found = True
                while (counter == len(d)):
                    if s[start] in d:
                        temp[s[start]] -= 1
                        if temp[s[start]] < d[s[start]]:
                            counter -= 1
                            curr = end - start + 1
                            if min_length > curr:
                                ans = [start,end]
                                min_length = curr
                    start += 1
            end += 1
            
        return s[ans[0] : ans[1] + 1] if found else ""
    
                    
            
        
