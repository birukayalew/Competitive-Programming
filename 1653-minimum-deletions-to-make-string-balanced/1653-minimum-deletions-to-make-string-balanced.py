class Solution:
    def minimumDeletions(self, s: str) -> int:
        invalid=0
        stack=[]
        for i in s:
            if i is 'b':
                stack.append(i)
            elif i is 'a' and stack==[]:
                continue
            elif i is 'a' and stack!=[]:
                invalid+=1
                stack.pop()
        return invalid