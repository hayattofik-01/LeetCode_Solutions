class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 1
        count = 0
        min_ = nums[0]
        
        for i in range(1, len(nums)):
            min_ &= nums[i]
        if min_ != 0:
            return 1

        cur = nums[0]
        while r < len(nums):
            if cur == min_:
                count += 1
                l = r
                cur = nums[l]
            else:
                cur &= nums[r]
            r += 1

        if cur == min_:
            count += 1

        return count