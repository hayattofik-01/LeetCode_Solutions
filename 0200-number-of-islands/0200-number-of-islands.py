class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n  or grid[i][j]=='0' or  grid[i][j] == "-v":
                return 0
            else:
                grid[i][j] = "-v"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                return 1
        m,n=len(grid),len(grid[0])
       
        ans=0
        for i in range(m):
            for j in range(n):
                if  grid[i][j]=='1':
                    
                    ans +=dfs(i,j)
        return ans