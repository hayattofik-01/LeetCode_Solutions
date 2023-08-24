class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        dxn = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def inBound(r,c):
            return 0 <= r < n and 0 <= c < n
        
        def dfs(r,c):
            if not inBound(r,c) or (r,c) in visited or not grid[r][c]:
                return 
            visited.add((r,c))
            for nr,nc in dxn :
                newR, newC = r + nr,c + nc
                dfs(newR,newC)
        def bfs():
            ans  = 0
            que = deque(visited)
            
            while que:
                
                length  = len(que)
                for i  in range(length):
                    r,c = que.popleft()
                    
                    for nr,nc in dxn :
                        
                        newR,newC = r + nr , c + nc
                        
                        if  not inBound(newR,newC) or (newR,newC) in visited:
                            continue
                            
                        if grid[newR][newC]:
                            return ans 
                        que.append((newR,newC))
                        visited.add((newR,newC))
                       
                ans +=1
            
            
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()
            
                
                
            
            
            
            
            
        
                    
                
            
            
        
        