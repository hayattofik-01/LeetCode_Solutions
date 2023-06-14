class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        
        
        def inBound(row,col):
            
            return 0 <= row < len(triangle) and 0 <= col < len(triangle[row])
        def dfs(row,col):
            
            if not inBound(row,col):
                return 0
            if row == len(triangle)-1:
                return triangle[row][col]
            if (row,col) in dp:
                return dp[(row,col)]
           
            dp[(row,col)] =  triangle[row][col] + min(dfs(row + 1,col),dfs(row + 1  ,col + 1))
            
            
            
            return dp[(row,col)]
        if len(triangle) == 1:
            return triangle[0][0]
        dfs(0,0)
        return dp[(0,0)]
      