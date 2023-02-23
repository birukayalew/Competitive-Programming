class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        dp=[collections.defaultdict(int) for i in range(n)]
        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                if diff in dp[j]:
                    dp[i][diff]=dp[j][diff]+1
                else:
                    dp[i][diff]=1
                ans=max(ans,dp[i][diff])
        return ans+1