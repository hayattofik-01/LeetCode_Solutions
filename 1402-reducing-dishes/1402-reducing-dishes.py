class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  # Sort in non-decreasing order
        n = len(satisfaction)
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