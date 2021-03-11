"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        info_store = defaultdict(lambda : 0)
        for i in range(len(employees)):
            info_store[employees[i].id] = employees[i] 
        
        return self.dfs(info_store,id)
        
    def dfs(self,info_store,id):
        
        employee_info = info_store[id]
        curr_value = employee_info.importance
        
        for i in employee_info.subordinates:
            curr_value += self.dfs(info_store,i)
            
        return curr_value


    
                
        
        
