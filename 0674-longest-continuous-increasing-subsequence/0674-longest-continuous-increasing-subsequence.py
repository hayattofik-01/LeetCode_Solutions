class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = 0
        r = 1 
        longest = 1
        while r < len(nums):
            if not  nums[r-1] < nums[r]:
                 l = r
            
                
            longest = max(longest, r - l + 1)
            r+=1
        return longest
        
        
        