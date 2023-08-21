class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        output =  [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        visited =  [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        dxn = [[0,1],[0,-1],[-1,0],[1,0]]
        que = deque()
        def inBound(r,c):
            return 0<= r < len(mat) and 0<= c < len(mat[0])
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    visited[r][c] = 1
                    que.append((r,c))
        while que:
            r ,c = que.popleft()
            
            for i,j in dxn :
                newr,newC = r + i ,c + j
                if inBound(newr,newC) and visited[newr][newC] != 1:
                    output[newr][newC] += output[r][c] + 1
                    visited[newr][newC] = 1
                    que.append((newr,newC))
        return output

                
        