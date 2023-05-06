class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        
        def dfs(node):
            
            visited.add(node)
            for  child in rooms[node]:
                if child not in visited:
                    dfs(child)
        dfs(0)
        if len(visited) != len(rooms):
            return False
        return True
            
            
        
        