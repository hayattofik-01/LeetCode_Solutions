class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i,memo,numS):
            
            if i  >= len(numS):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] =max (dfs(i+2,memo,numS) + numS[i],dfs(i+1,memo,numS))
            
            return memo[i]
        if len(nums)== 1:
            return nums[0]
        else:
            return max(dfs(0,{},nums[:len(nums)-1]),dfs(0,{},nums[1:]))
            
            
            
            
                
        
        
    