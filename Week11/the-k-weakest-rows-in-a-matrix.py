class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        answer = []
        for i in range(len(mat)):
            soldier = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    soldier += 1
            temp.append([soldier,i])
        temp.sort()
        for i in range(k):
            answer.append(temp[i][1])
        return answer
                    
