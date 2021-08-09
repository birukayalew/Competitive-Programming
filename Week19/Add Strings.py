class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        summation = 0
        remainder = 0
        ans = []
        start1 = len(num1) - 1
        start2 = len(num2) - 1
        
        while start1 >= 0 or start2 >= 0 or remainder > 0:
            
            value1 = num1[start1] if start1 >= 0 else 0
            value2 = num2[start2] if start2 >= 0 else 0
            
            summation =  int(value1) + int(value2) + remainder
            if summation >= 10:
                remainder = summation // 10
                ans.append(str(summation % 10))
            else:
                remainder = 0
                ans.append(str(summation))
            start1 -= 1
            start2 -= 1
            
        ans.reverse()
        return "".join(ans)
        
