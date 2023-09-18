class Solution:
    def minSteps(self, n: int) -> int:
        
        cache = defaultdict(int)
        def dp( onstack, cur):
          
            if cur > n:
                return float('inf')
            if cur == n:
                return 0
            cp = dp(cur, cur + cur) +   2
            p = float('inf')
            if onstack:
                p = dp(onstack, cur + onstack) + 1
            cache[(onstack,cur)] = min(p,cp)
                
            return  cache[(onstack,cur)] 
                
            
    
        return dp(0,1)
        
            
            
            
        