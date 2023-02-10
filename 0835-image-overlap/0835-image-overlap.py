class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        bits1 = [int("".join(str(b) for b in row), base=2) for row in img1]
        bits2 = [int("".join(str(b) for b in row), base=2) for row in img2]
        bits2 = ([0] * (n-1)) + bits2 + ([0] * (n-1))
        ansl = ansr = 0 
        for y in range(len(bits2)-len(bits1)+1):
            for x in range(n):
                cntl = cntr = 0
                for i in range(n):
                    row1 = bits1[i]
                    row2 = bits2[i+y]
                    cntl += ((row1 >> x) & row2).bit_count()
                    cntr += (row1 & (row2 >> x)).bit_count()
                ansl = max(ansl, cntl)
                ansr = max(ansr, cntr)
        return max(ansl, ansr)