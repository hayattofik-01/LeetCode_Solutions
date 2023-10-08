class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        l = n - 1
        r = n - 1

        while l > 0:
            l -= 1
            if l + nums[l] >= r:
                r = l

        return r == 0