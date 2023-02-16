class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        roman1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roman2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        for i in range(len(s)):
            if((i!=(len(s)-1)) and ((s[i]+s[i+1]) in roman2.keys())):
                result+=roman2[s[i]+s[i+1]]
            else:
                if((i==0) or ((i>0) and ((s[i-1]+s[i]) not in roman2.keys()))):
                    result+=roman1[s[i]]
        return result