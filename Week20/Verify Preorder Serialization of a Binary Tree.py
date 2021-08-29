class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        stack = []
        for i in range(len(preorder)):
            stack.append(preorder[i])
            while (len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#'):
                stack.pop(-1)
                stack.pop(-2)
                stack[-1] = '#'
                
        return True if len(stack) == 1 and stack[-1] == '#' else False
        
