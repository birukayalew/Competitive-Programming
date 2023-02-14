class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        half = total // 2
        n = len(nums)        
        @functools.lru_cache(None)
        def options(i, to_pick):
            if not to_pick:
                return [0]
            if i == n:
                return []
            it = heapq.merge(options(i + 1, to_pick), [e + nums[i] for e in options(i + 1, to_pick - 1)])
            return [k for k, _ in itertools.groupby(it)]
        
        @functools.lru_cache(None)
        def dp(i, to_pick, target):
            if not to_pick:
                return 0
            if i == n:
                return math.inf
            if i < n // 2:
                ans1 = dp(i + 1, to_pick, target)
                ans2 = dp(i + 1, to_pick - 1, target - nums[i]) + nums[i]
                diff1 = abs(target - ans1)
                diff2 = abs(target - nums[i] - dp(i + 1, to_pick - 1, target - nums[i]))
                if diff1 < diff2:
                    return ans1
                elif diff1 == diff2:
                    return max(ans1, ans2)
                else:
                    return ans2
            else:
                op = options(i, to_pick)
                index = bisect.bisect(op, target)
                ans = math.inf
                if index < len(op):
                    ans = op[index]
                if index and abs(op[index - 1] - target) < abs(ans - target):
                    ans = op[index - 1]
                return ans
        
        closest = dp(1, n // 2 - 1, half - nums[0]) + nums[0]
        return abs(total - 2 * closest)