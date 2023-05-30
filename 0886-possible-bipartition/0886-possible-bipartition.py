class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = [ 0 for i in range(n)]
        adj_lis = defaultdict(list)
        visited = set()
        for i,j in dislikes:
            adj_lis[i].append(j)
            adj_lis[j].append(i)
        
        def dfs(node,color):
            ans = True
            for child in adj_lis[node]:
                
                if child in visited  and colors[child-1] == color:
                    return False
                if child not in visited:
                    visited.add(child)
                    colors[child-1 ] = -1 * color 
                    ans = ans and dfs(child,colors[child-1])
            return ans
        
        
        ans = True
        for i in range(1,n+1):
            if i not in visited:
                visited.add(i)
                colors[i-1] = 1
                ans = ans and dfs(i,1)
        return ans 
        
    
                
        