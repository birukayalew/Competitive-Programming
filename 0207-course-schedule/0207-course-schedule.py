class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        visiting = set()
        for ai, bi in prerequisites:
            graph[bi].append(ai)

        def has_cycle(course, visited, visiting):
            if course in visiting: 
                return True  
            if course in visited: 
                return False

            visiting.add(course)  # Move this line BEFORE the loop

            for neighbor in graph[course]: 
                if has_cycle(neighbor, visited, visiting): 
                    return True  

            visiting.remove(course)  
            visited.add(course) 
            return False 
       
        for course in range(numCourses):
            if course not in visited and has_cycle(course, visited, visiting):
                return False
        return True