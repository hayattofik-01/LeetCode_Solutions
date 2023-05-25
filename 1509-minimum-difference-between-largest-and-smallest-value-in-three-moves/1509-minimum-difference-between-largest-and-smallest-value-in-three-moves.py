class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <=4:
            return 0
        n = len(nums)
        nums.sort()
        min1 = min((nums[n - 4] - nums[0]),(nums[n-1]- nums[3]))
        min2 = min((nums[n - 3] - nums[1]),(nums[n-2] - nums[2]))
        ans = min(min1 ,min2)
        return ans