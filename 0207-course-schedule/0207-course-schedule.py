class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree= [0 for i in range(numCourses)]
        adj_list=defaultdict(list)
        order =[]
        for d,I in prerequisites:
            adj_list[I].append(d)
            inDegree[d] +=1
            
            
        visited = set()
        que = deque()
       
            
        
        for val in range(numCourses):
            if inDegree[val] == 0:
                que.append(val)
                             
        while que:
                
                node = que.popleft()
                order.append(node)
                for child in adj_list[node]:
                    inDegree[child]-=1
                    if child not in visited and inDegree[child] == 0:
                        que.append(child)
                        visited.add(child)
                             
      
     
        if len(order) != numCourses:
            return False
        return True
        
                
        
        