class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largestSum = nums[0]
        
        for  i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] +=nums[i - 1]
            largestSum = max(nums[i],largestSum)
        return largestSum
            
