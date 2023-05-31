class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo= [[0 for i in range(n)] for i in range(m) ]
        print(memo)
        def inBound(i,j):
            if  0 <=  i < m and 0 <= j < n:
                return memo[i][j]
            return 0
        
       
        memo[0][0] = 1
        
        for r in range(m):
            
            for c in range(n):
                
                memo[r][c] += inBound(r - 1,c) + inBound(r,c-1)
                
        return memo[m-1][n-1]
                
                
                