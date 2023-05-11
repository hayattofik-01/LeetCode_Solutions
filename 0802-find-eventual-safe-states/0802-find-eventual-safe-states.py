class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_lis = defaultdict(list)
        outDegree = defaultdict(int)
        que = deque()
        visited = set()
        ans=[]
        for i  in range(len(graph)):
            if not graph[i]:
                que.append(i)
                ans.append(i)
               
            
            
            for num in graph[i]:
                outDegree[i]+=1
                adj_lis[num].append(i)
    
        while que:
            node = que.popleft()
          
         
            for child in adj_lis[node]:
                outDegree[child]-=1
                if outDegree[child] == 0:
                    que.append(child)
                    ans.append(child)
          
                  
     
        return sorted(ans)
                    
        
        
        
        
                
                
                
            
        