
# topological sort and BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = {}
        queue = deque()
        store = []
        for i in range(numCourses):
            store.append(0)
        for i in range(len(prerequisites)):
            store[prerequisites[i][0]] += 1
            if prerequisites[i][1] in dependency:
                dependency[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                dependency[prerequisites[i][1]] = [prerequisites[i][0]]
        for i in range(len(store)):
            if store[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            if curr in dependency:
                for i in dependency[curr]:
                    store[i] -= 1
                    if store[i] == 0:
                        queue.append(i)
        for i in store:
            if i != 0:
                return False
        return True
            
        
        
        
        
