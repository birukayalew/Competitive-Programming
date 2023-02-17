class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        dq=deque()
        n=len(nums)
        mn,mx=-1,-1
        ans=0
        for i in range(n):
            if minK<=nums[i]<=maxK:
                dq.append(i)
                if nums[i]==minK:
                    mn=i
                if nums[i]==maxK:
                    mx=i
                if mn!=-1 and mx!=-1:
                    ans+=min(mn,mx)-dq[0]+1
            else:
                while dq:
                    dq.popleft()
                mn,mx=-1,-1
        return ans