class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def converter(s):
            ans = 0
            for i in range(len(s) - 1, -1, -1):
                ans += (int(s[i]) * (2 ** (len(s) - i - 1)))
                
            return ans
        
        return bin(converter(a) + converter(b))[2:]