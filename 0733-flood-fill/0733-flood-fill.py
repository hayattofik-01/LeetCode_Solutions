class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        
        def dfs(i,j,const):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return 
            if image[i][j] != const or (i,j) in visited:
                return 
            
            visited.add((i,j))
            image[i][j] = color
            dfs(i+1,j,const)
            dfs(i-1,j,const)
            dfs(i,j-1,const)
            dfs(i,j+1,const)
            
        const = image[sr][sc]
       
        dfs(sr,sc,const)
        return image

        
        
        
        