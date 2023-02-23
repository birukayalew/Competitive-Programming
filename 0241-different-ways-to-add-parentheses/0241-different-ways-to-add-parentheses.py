class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not expression: return []
        if expression.isdigit(): return [int(expression)]
        mylist = []
        for i in range(len(expression)):
            if expression[i] not in ['+','-','*']: continue
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i+1:])
            for l in left:
                for r in right:
                    if expression[i]=='+': mylist.append(l+r)
                    elif expression[i]=='-': mylist.append(l-r)
                    elif expression[i]=='*': mylist.append(l*r)
        return mylist