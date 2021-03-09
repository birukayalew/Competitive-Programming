class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        answer = ""
        for i in range(len(s)):
            
            
            if len(stack) == 0:
                stack.append([s[i],1])
            else:
                if stack[-1][0] == s[i]:
                    stack[-1][1] += 1
                if stack[-1][0] != s[i]:
                    stack.append([s[i],1])
                if stack[-1][1] == k:
                    
                    stack.pop()
                    
        for i in range(len(stack)):
            for j in range(stack[i][1]):
                answer += stack[i][0]
        return answer
            
                
