class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        w = 0
        ans = float('inf')
        while r < len(blocks):
            if blocks[r] == 'W':
                w += 1
            if r - l == k - 1:
                ans = min(ans, w)
                if blocks[l] == 'W':
                    w -= 1
                l += 1
            r += 1
        return ans