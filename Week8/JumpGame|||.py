class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        queue = deque()
        visited = set()
        visited.add(start)
        queue.append(start)
        while queue:
            poped = queue.popleft()
            if arr[poped] == 0:
                return True
            
            directions = [-1,1]
            for i in directions:
                path = poped + arr[poped] * i
                if path not in visited and 0 <= path < len(arr):
                    queue.append(path)
                    visited.add(path)
        return False
