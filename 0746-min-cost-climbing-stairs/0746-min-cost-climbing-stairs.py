class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        
        def dp(n):
            
            if n >= len(cost):
                return 0
            
            if n in memo:
                return memo[n]
            
            memo[n] =  min(cost[n] + dp(n+1),cost[n]+ dp(n+2))
            
            return memo[n]
        
                          
        return min (dp(0),dp(1))
            
        