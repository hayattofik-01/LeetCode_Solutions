class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = 0
        dp = {}
        def dfs(remain):
            nonlocal ans
           
            if remain < 0:
                return 0
            if remain == 0:
                
                return 1
            if remain in dp:
                
                return dp[remain]
            
            ans = 0
            for j in range(len(nums)):
                ans += dfs(remain - nums[j])
            dp[remain] = ans  
            return ans
            
                
            
        return dfs(target)
                
        