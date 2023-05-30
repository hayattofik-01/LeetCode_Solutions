class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ans = 0
        memo = {}
        def dfs(i,Sum):
            nonlocal ans  
            
            if i >= len(nums):
                if Sum == target:
                    ans+=1
                    return 1
                return 0
            
            if (i,Sum) in memo:
                return memo[(i,Sum)]
            
            memo[(i,Sum)]= dfs(i+1,Sum + nums[i]) + dfs(i+1,Sum - nums[i])
            
            # memo[(i,Sum)] = 
    
            return memo[(i,Sum)]
    
        return dfs(0,0)
        

    
     
                
            
        