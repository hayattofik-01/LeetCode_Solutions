class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dxn = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m, n = len(grid2), len(grid2[0])
        count = 0

        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(row, col):
            if not inBound(row, col) or grid2[row][col] == 0:
                return True
            if grid1[row][col] == 0:
                return False
            grid2[row][col] = 0  # Mark the cell as visited in grid2
            is_sub_island = True
            for i, j in dxn:
                newR, newC = row + i, col + j
                is_sub_island &= dfs(newR, newC)
            return is_sub_island

        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    if dfs(row, col):
                        count += 1
        return count