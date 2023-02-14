class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n - 1):
            ans.append(i)
        if ans and sum(ans) == 0: 
            ans[-1] += 1
        ans.append(-1*sum(ans))
        return ans 