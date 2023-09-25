class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        def inBound(r,c):
            return 0 <= r < len(dungeon) and 0 <= c < len(dungeon[0])
        
        for i in range(len(dungeon) - 1, -1, -1):
            for j in range(len(dungeon[0]) - 1, -1 ,-1):
                if not inBound(i,j + 1) and not inBound(i + 1, j):
                    dungeon[i][j] = min(0, dungeon[i][j])
                elif not inBound(i + 1,j) :
                    dungeon[i][j] += dungeon[i] [j + 1]
                    
                elif not inBound(i,j + 1):
                    dungeon[i][j] += dungeon[i + 1][j]
                
                else:
                    dungeon[i][j] += max(dungeon[i][j + 1],dungeon[i + 1][j])
                if dungeon[i][j] > 0:
                    dungeon[i][j] = 0
        print(dungeon)
        return abs(dungeon[0][0]) + 1
                    
                
                        
                    
                    
                
        
       