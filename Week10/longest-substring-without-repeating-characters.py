class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)
        
        seen = {}
        starter_index = 0
        seen[s[starter_index]] = starter_index
        end = 1
        max_length = 1
        
        while end < len(s):
            if s[end] in seen:
                if seen[s[end]] >= starter_index:
                    max_length = max(max_length,end - starter_index)
                    starter_index = seen[s[end]] + 1 
            seen[s[end]] = end
            end += 1
        max_length = max(max_length,end - starter_index)
        return max_length
