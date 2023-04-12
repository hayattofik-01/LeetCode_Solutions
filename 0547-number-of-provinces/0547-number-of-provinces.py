class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(node):
            nonlocal visited
            if node in visited:
                return 
            
            visited.add(node)
            for child in adj_list[node]:
              
                    dfs(child)
        count =0
        adj_list =defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
      
                
        for node in adj_list:
            if node not in visited:
                dfs(node)
                count +=1
        return count
            
             
            