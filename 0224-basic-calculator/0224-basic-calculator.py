class Solution:
    def calculate(self, s: str) -> int:
        precedence = {'+':1, '-':1, "~":1, '(':2, ")":0}        
        operator = []
        num = ""
        postfix = []
        
        is_start = True
        for char in s:
            if char == " ":
                continue
            
            if char.isdigit():
                num += char
                is_start = False
            elif is_start and char not in "()":
                operator.append("~")
                is_start = False
            else:
                if num:
                    postfix.append(num)
                    num = ""
                    
                if char == ")":
                    while operator and operator[-1] != "(":
                        postfix.append(operator.pop())
                    
                    operator.pop()
                else:
                    while (operator and operator[-1] != "(" and
                           precedence[operator[-1]] >= precedence[char]):
                        postfix.append(operator.pop())
                    operator.append(char)                
                    
                    if char == "(":
                        is_start = True
                        
        if num:
            postfix.append(num)
        
        postfix.extend(operator)        
        stack = []
        
        for ex in postfix:
            if ex in "+-": 
                y, x = stack.pop(), stack.pop()
                stack.append(self.evaluate(x, y, ex))
            elif ex == "~":
                stack.append(str(-1 * int(stack.pop())))
            else:
                stack.append(ex)
        return int(stack.pop())
     
    
    def evaluate(self, x, y, op):
        result = 0
        if op == "+":
            result = int(x) + int(y)
        elif op == "-":
            result = int(x) - int(y)
        return str(result)