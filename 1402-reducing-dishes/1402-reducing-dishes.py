class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  # Sort in non-decreasing order
        n = len(satisfaction)
        prefix_sum = [0] * (n + 1)  # Prefix sum array

        # Calculate prefix sum
        for i in range(n - 1, -1, -1):
            prefix_sum[i] = satisfaction[i] + prefix_sum[i + 1]

        max_cof = 0

        # Calculate maximum like-time coefficient
        for i in range(n):
            time = 1
            cof = 0
            for j in range(i, n):
                cof += time * satisfaction[j]
                time += 1
            max_cof = max(max_cof, cof)

        return max_cof