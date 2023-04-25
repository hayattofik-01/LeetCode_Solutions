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
        
       
        self.memor = defaultdict(list)
       
        for emp in employees:
            self.memor[emp.id].append(emp.importance)
            self.memor[emp.id].append(emp.subordinates)
        Sum =self.memor[id][0]
        
        def dfs(idx):
            nonlocal Sum
            Sum = self.memor[idx][0]
            for i in self.memor[idx][1]:
                Sum +=dfs(i)
            return Sum
            
                
            
        return dfs(id)