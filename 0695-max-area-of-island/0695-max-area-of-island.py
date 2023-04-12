class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])
        maxArea = 0

        def island(x, y):
            area = 0
            if x < 0 or x >= maxRow or y < 0 or y >= maxCol or grid[x][y] != 1:
                return area
            grid[x][y] = 0
            area += 1
            for newx,newy in [[1,0], [-1,0], [0,1], [0,-1]]:
                area += island(x+newx, y+newy)
            return area

        for row in range(maxRow):
            for col in range(maxCol):
                if grid[row][col]:
                    maxArea = max(maxArea, island(row, col))
        return maxArea