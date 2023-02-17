class Solution:
    def firstUniqChar(self, s: str) -> int:
        d =  {}
        for i, l in enumerate(s):
            if l in d:
                d[l] = -1
            else:
                d[l] = i
        for i, l in enumerate(s):
            if d[l] != -1:
                return i
        return -1