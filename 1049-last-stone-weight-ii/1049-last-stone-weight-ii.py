class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = math.ceil(sum(stones)/2)
        fsum = float('inf')
        dp = defaultdict(int)
        def dfs(cur,sum_):
            nonlocal fsum
            if sum_ >= target:
                fsum = min(sum_,fsum)
                return fsum
            if cur >= len(stones):
                return fsum
            if (cur,sum_) in dp:
                return dp[(cur,sum_)]
            
            dp[(cur,sum_)] = min(dfs(cur+ 1,sum_ + stones[cur]),dfs(cur + 1,sum_))
            return dp[(cur,sum_)]
            
        dfs(0,0) 
        remain = sum(stones) - fsum 
        
        return abs(remain - fsum )
            
        
        
    
      
        
        
        