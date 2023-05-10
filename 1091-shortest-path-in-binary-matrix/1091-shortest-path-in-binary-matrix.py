class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        que= deque()
        dxn = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        if grid[0][0] == 0:
            que.append((0,0,1))
            visited.add((0,0))
        def inBound(row,col):
            return  0 <= row < len(grid) and 0<= col <len(grid[0])
                
        while que:
            row,col,level = que.popleft()
            if row == len(grid)-1 and col == len(grid[0]) -1:
                return level
          
            level += 1
            for  i,j in dxn :
                new_row,new_col = row + i,col + j
                
                if inBound(new_row,new_col) and grid[new_row][new_col] ==0 and  (new_row,new_col) not in visited:
                    que.append((new_row,new_col,level))
                    visited.add((new_row,new_col))
        return -1
                    
                    
                    