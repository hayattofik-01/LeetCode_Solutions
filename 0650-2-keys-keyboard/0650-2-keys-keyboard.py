class Solution:
    def minSteps(self, n: int) -> int:
        
        ans = 0 
        def dp( onstack, cur):
            nonlocal ans 
          
            if cur > n:
                return float('inf')
            if cur == n:
                return 0
            cp = dp(cur, cur + cur) +   2
            p = float('inf')
            if onstack:
                p = dp(onstack, cur + onstack) + 1
                
            return min(p,cp)
                
            
    
        return dp(0,1)
        
            
            
            
        