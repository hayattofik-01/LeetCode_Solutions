class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_lis = defaultdict(list)
        n = len(graph)-1
        self.output =[]
        
        def dfs(val,soln):
            if n == val:
                self.output.append(soln.copy())
                return 
            if not graph[val]:
               
                return
            for v in graph[val]:
               
                soln.append(v)
                
                dfs(v,soln)
                if soln:
                    soln.pop()
        dfs(0,[0])
        return self.output
                
            
            
       
        