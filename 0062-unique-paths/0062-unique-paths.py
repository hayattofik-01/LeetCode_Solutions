class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = 0
        memo = {}
        def inBound(i,j):
            return 0 <=  i < m and 0 <= j < n
        
        def dfs(i,j):
            nonlocal path
            if not inBound(i,j):
                return 0 
            if (i,j) == (m-1,n-1):
               
                return  1
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dfs(i + 1, j) + dfs(i,j + 1)
            
            
            return memo[(i,j)]
        
        return dfs(0,0)
        