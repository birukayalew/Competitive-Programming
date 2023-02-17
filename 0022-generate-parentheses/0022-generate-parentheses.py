class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def valid(parentheses):
            stack = []
            for i in range(len(parentheses)):
                if parentheses[i] == '(':
                    stack.append(parentheses[i])
                else:
                    if not stack:
                        return False
                    stack.pop()
            return True if not stack else False

        def helper(idx, temp):
            if idx == 2 * n:
                if valid(temp):
                    s = "".join(temp[:])
                    ans.append(s)
                return

            helper(idx + 1, temp + ['('])
            helper(idx + 1, temp + [')'])

        helper(0, [])
        return ans

