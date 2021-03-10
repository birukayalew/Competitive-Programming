class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed_index = 0
        popped_index = 0
        
        while pushed_index < len(pushed):
            stack.append(pushed[pushed_index])
            while stack and popped_index < len(popped) and popped[popped_index] ==  stack[-1]:
                stack.pop()
                popped_index += 1
            pushed_index += 1
                
        return len(stack) == 0
                
            
        
