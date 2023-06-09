class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        
        def inBound(i):
            
            return 0 <= i < len(prices)
    
    
        def dfs(i, buy):
            
            if not inBound(i):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            
            if buy:
                
                profit = max(- prices[i] + dfs(i + 1,0),dfs(i+1,1))
               
            else:
                profit = max( prices[i] - fee  + dfs(i+1,1),dfs(i+ 1, 0) )
               
            
            memo[(i,buy)] = profit
            return memo[(i,buy)]
        return dfs(0,1)
            
        
       