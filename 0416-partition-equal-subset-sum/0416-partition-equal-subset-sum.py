class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target/2
        def dfs(i,total):
            if i >= len(nums):
                return False
            if total == target:
                return True
            if total > target:
                return False
            if (i,total) in dp:
                return dp[(i,total)]
        
            cur = False
            dp[(i,total)] = cur or dfs(i + 1,total + nums[i]) or dfs(i + 1 ,total)
            
            return dp[(i,total)]
            
            
            
        return dfs(0,0)
                
        