class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1] * 1001 for _ in range(n)]
        max_length = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                max_length = max(max_length, dp[i][diff])
        return max_length
        