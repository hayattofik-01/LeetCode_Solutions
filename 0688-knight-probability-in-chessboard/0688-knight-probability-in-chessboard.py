class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = [[[-1] * k for _ in range(n)] for _ in range(n)]
    
        def dfs(row, col, moves):
            if row < 0 or col < 0 or row >= n or col >= n:
                return 0
            if moves == k:
                return 1
            if memo[row][col][moves] != -1:
                return memo[row][col][moves]

            total_prob = 0
            for dx, dy in [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]:
                total_prob += dfs(row + dx, col + dy, moves + 1)

            memo[row][col][moves] = total_prob / 8
            return memo[row][col][moves]
    
        return dfs(row, column, 0)
        