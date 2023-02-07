class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for ops in logs:
            if ops == '../':
                ans -= 1
            elif ops == './':
                continue
            else:
                ans += 1
            ans = max(0, ans)
        return ans