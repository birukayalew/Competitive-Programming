class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = len(s) - 1
        for i in range(len(t) - 1,-1,-1):
            if index < 0:
                return True
            if s[index] == t[i]:
                index -= 1
        if index < 0:
            return True
        return False
        
