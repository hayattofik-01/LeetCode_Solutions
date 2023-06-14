class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}
        def inBound(i):
            return 0 <= i < len(questions)
        
        def dfs(i):
          
            if not inBound(i) :
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] =  max(questions[i][0] + dfs(i + questions[i][1] + 1), dfs(i+1))
            return dp[i]

            
          
        return dfs(0)
        