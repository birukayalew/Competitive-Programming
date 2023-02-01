class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        temp = []
        for i in range(len(plantTime)):
            temp.append([plantTime[i], growTime[i]])
        temp.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        st = 0
        for p, g in temp:
            st += p
            ans = max(ans, st + g)
        return ans