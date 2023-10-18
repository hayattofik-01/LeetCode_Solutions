class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        diff = max_num - min_num
        
        # Check if the difference is already less than 2k
        if diff <= 2 * k:
            return 0
        
        # Reduce the difference by applying operations
        return diff - 2 * k