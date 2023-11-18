class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxn = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def backtrack(row, col, i):
            if i == len(word):
                return True
            if not inbound(row, col) or (row,col) in visited:
                return False
            if board[row][col] != word[i]:
                return False
            

            
            cur = False
            visited.add((row,col))
            for r, c in dxn:
                new_r, new_c = row + r, col + c

                cur = cur or backtrack(new_r, new_c, i + 1)
            visited.remove((row,col))
            return cur

        for i in range(len(board)):
            for j in range(len(board[0])):
                ans = backtrack(i, j, 0)
                if ans:
                    return True

        return False