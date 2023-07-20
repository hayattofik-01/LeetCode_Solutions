class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dp = {}
        def dfs(i,cur):
            
            if i  >= len(prices):
                return 0 
            if (i,cur) in dp:
                return dp[(i,cur)]
            if cur == "b":
                dp[(i,cur)] = max(profit - prices[i]  + dfs(i + 1 , "s"), dfs(i + 1, cur))
            if cur ==  "s": 
                dp[(i,cur)] = max(profit + prices[i] + dfs(i + 1, "c"),dfs(i + 1 , cur ))
            if cur == "c": 
                dp[(i,cur)] = dfs(i+1 ,"b")
                
            return dp[(i,cur)]
        return dfs(0,"b")
                
        