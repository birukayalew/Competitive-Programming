class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        if len(s) == 1:
            return 1
        last_index = defaultdict(lambda: -1)
        l, r = 0, 0
        ans = float('-inf')
        while r < len(s):
            if l <= last_index[s[r]] <= r:
                ans = max(ans, r - l)
                l = last_index[s[r]] + 1
                last_index[s[r]] = r
            else:
                last_index[s[r]] = r
            r += 1
        ans = max(ans, r - l)
        return 0 if ans == float('-inf') else ans
        
        
        