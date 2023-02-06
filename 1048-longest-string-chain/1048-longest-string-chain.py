class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        given = []
        dp = defaultdict(int)
        for s in words:
            given.append([len(s), s])
        given.sort()
        
        def check(pre, curr):
            for i in range(len(curr)):
                temp = curr[:i] + curr[i+1:]
                if temp == pre:
                    return True
            return False
            
            
        for i in range(len(given)):
            res = 0
            for j in range(i):
                if len(given[i][1]) - len(given[j][1]) == 1  and check(given[j][1], given[i][1]):
                    res = max(res, dp[given[j][1]])
                    
            dp[given[i][1]] = res + 1
            
        
        return max(dp.values()) 