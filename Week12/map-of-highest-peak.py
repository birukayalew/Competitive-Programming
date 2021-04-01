class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row = len(isWater)
        col = len(isWater[0])
        answer = [[float('inf') for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    queue.append((0,i,j))
                    answer[i][j] = 0
        while queue:
            height,i,j = queue.popleft()
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for move in directions:
                new_i = i + move[0]
                new_j = j + move[1]
                if 0 <= new_i < row and 0 <= new_j < col:
                    if height + 1 < answer[new_i][new_j]:
                        answer[new_i][new_j] = height + 1
                        queue.append((height + 1,new_i,new_j))
        return answer
