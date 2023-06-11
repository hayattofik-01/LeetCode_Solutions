class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        dp = {}
        ans = 0
        
        for num in arr:
            
            count = 1
            if num - difference in dp:
                count +=dp[num - difference]
            dp[num] = count
            ans = max(ans,dp[num])
        return ans
            
            
                
        
        
       