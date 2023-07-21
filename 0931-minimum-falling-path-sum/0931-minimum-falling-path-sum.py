class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        directions = [(1, -1), (1, 0), (1, 1)]

        def inBound(i, j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

        def dfs(i, j):
            if not inBound(i, j):
                return float('inf')
            if memo[i][j] is not None:
                return memo[i][j]
            if i == len(matrix) - 1:
                return matrix[i][j]

            min_sum = float('inf')
            for l, m in directions:
                min_sum = min(min_sum, dfs(i+l, j+m))

            memo[i][j] = matrix[i][j] + min_sum
            return memo[i][j]

        min_sum = float('inf')
        for c in range(len(matrix[0])):
            min_sum = min(min_sum, dfs(0, c))

        return min_sum


