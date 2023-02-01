class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        temp = []
        ans = 0
        for i in range(len(scores)):
            temp.append([ages[i], scores[i], scores[i]])
        temp.sort()
        
        for i in range(len(temp)):
            cur_total = temp[i][1]
            for j in range(i - 1, -1, -1):
                if temp[i][1] >= temp[j][1]:
                    cur_total = max(cur_total, temp[i][1] + temp[j][2])
            temp[i][2] = cur_total
            ans = max(ans, cur_total)
            
        return ans
    
        
        