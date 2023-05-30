class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(remain, cache):
            
            if remain < 0:
                return float('inf')
            
            if remain == 0 :
                
                return 0
            
            if remain in cache:
                return cache[remain]
            
            cache[remain] = min(dfs(remain - val , cache) + 1 for val in coins)
            
            return cache[remain]
        
        ans = dfs(amount,{})
        
        if ans == float('inf'):
            return -1
        return ans
        
        