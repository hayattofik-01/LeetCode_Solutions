class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9  + 7
        
        dp = [[0 for sum_ in range(target + 1)] for dices in range(n + 1)]
        dp[0][0] = 1
        for dices in range(1,n + 1):
            for sum_ in range(target + 1):
                
                for prev in range(1,min(k,sum_) + 1):
                    dp[dices][sum_] += dp[dices - 1][sum_ - prev]
                    dp[dices][sum_] %= mod
        return dp[n][target]
         
                
        