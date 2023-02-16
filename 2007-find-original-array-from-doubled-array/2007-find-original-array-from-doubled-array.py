class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        d = defaultdict(int)
        zeros = 0
        ans = []
        changed.sort()
        for num in changed:
            d[num] += 1
            if num == 0:
                zeros += 1
        if zeros % 2 == 1:
            return []
        for i, num in enumerate(changed):
            if d[num] > 0:
                if d[num * 2] > 0:
                    d[num] -= 1
                    d[num * 2] -= 1
                    ans.append(num)
                else:
                    return []
        return ans