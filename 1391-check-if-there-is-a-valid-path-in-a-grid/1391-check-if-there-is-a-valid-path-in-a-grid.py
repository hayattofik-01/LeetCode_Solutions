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
        
        for row in range(len(grid)):
             for col in range(len(grid[0])):
                parent[(row,col)] = (row,col)
        def inBound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def findRoot(row, col):
           
            while parent[(row,col)] != (row,col):
                
                row, col =  parent[(row,col)][0],parent[(row,col)][1]
            return (row,col)
        def union(cell1,cell2):
            
            rootC1 = findRoot(cell1[0],cell1[1])
            rootC2 = findRoot(cell2[0],cell2[1])
            
            if rootC1 != rootC2:
                
                parent[rootC1] = rootC2
                
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # constant time
                
                for dxn in dxnRef[grid[row][col]]:
                   
                    new_r ,new_c = row + dxn[0],col + dxn[1]
                   
                    if inBound(new_r,new_c) and (-1* dxn[0],-1* dxn[1]) in dxnRef[grid[new_r][new_c]]:
                       
                            
                            union((row,col),(new_r,new_c))
        m  = len(grid) -1
        n = len(grid[0]) -1
        if  findRoot(0,0) == findRoot(m,n):
            return True
        return False
                
                
        
        
            
    
        
        