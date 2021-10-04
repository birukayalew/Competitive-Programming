class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        d = {}
        arr = [0 for x in range(26)]
        for i in range(length):
            arr[ord(s1[i]) - ord('a')] += 1
        d["s1"] = arr
        
        left = 0
        right = 0
        while right < len(s2):
            temp = [0 for x in range(26)]
            while right < len(s2) and (right - left) != length:
                temp[ord(s2[right]) - ord('a')] += 1
                right += 1
            if temp == d['s1']:
                return True
            if right >= len(s2):
                return False
            left += 1
            right = left
        return False
            
