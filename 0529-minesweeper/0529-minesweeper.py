class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dxn = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
        
        def inBound(row,col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        def dfs(row,col):
            
            if not inBound(row,col) :
                return 
            if board[row][col] == 'M':
                board[row][col] = 'X'
                return 
            
            if board[row][col] == 'E':
                count = 0
                for r,c in dxn :
                    newR,newC = row + r, col + c
                    if inBound(newR,newC) and board[newR][newC] == 'M':
                        count +=1
                if count > 0 :
                    board[row][col] = str(count )
                
                else:
                    board[row][col] = 'B'
                    for r,c in dxn :
                        newR,newC = row + r, col + c
                        if inBound(newR,newC) and board[newR][newC] == 'E':
                            dfs(newR,newC)
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        if board[click[0]][click[1]] == 'E':
            dfs(click[0],click[1])
        return board
            
            
                
                
            
            
            
       