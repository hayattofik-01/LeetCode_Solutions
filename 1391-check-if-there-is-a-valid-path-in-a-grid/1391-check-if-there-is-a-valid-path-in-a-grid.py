class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dxnRef = defaultdict(set)
        dxnRef[1].update({(0,-1),(0,1)})
        dxnRef[2].update({(-1,0),(1,0)})
        dxnRef[3].update({(0,-1),(1,0)})
        dxnRef[4].update({(0,1),(1,0)})
        dxnRef[5].update({(-1,0),(0,-1)})
        dxnRef[6].update({(-1,0),(0,1)})
    
        parent = defaultdict(tuple)
        size = {}
        
        for row in range(len(grid)):
             for col in range(len(grid[0])):
                parent[(row,col)] = (row,col)
                size[(row,col)] = 1
                
        def inBound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def find(cell):
            
            if parent[cell] != cell:
                parent[cell] = find(parent[cell])
            
            return parent[cell]
           
        def union(cell1,cell2):
            
            rootC1 = find(cell1)
            rootC2 = find(cell2)
            
            if rootC1 != rootC2:
                
                if size[rootC1] >= size[rootC2]:
                    parent[rootC2] = rootC1
                    size[rootC1] += size[rootC2]
                else:
                    parent[rootC1] = rootC2
                    size[rootC2] += size[rootC1]
                    
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # constant time
                
                for dxn in dxnRef[grid[row][col]]:
                   
                    new_r ,new_c = row + dxn[0],col + dxn[1]
                   
                    if inBound(new_r,new_c) and (-1* dxn[0],-1* dxn[1]) in dxnRef[grid[new_r][new_c]]:
                            union((row,col),(new_r,new_c))
                            
        m  = len(grid) -1
        n = len(grid[0]) -1
        
        return find((0,0)) == find((m,n))
        
        