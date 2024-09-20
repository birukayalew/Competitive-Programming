class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        
        if not s:
            return 0
        d = defaultdict(int)
        
        length = 1
        l, r = 0, 0
        while r < len(s):
            if d[s[r]]:
                while d[s[r]]:

                    d[s[l]] = 0
                    l += 1
            length = max(length, r - l + 1)
            d[s[r]] = 1
            r += 1
        length = max(length, r - l)

        return length
    
    
    