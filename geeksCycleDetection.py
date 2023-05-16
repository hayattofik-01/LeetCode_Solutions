
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
	
		def dfs(node,parent):
		    
		    for child in adj[node]:
		        if child not in visited:
		            visited.add(child)
		            
		      
		            ans = dfs(child,node)
		            if ans:
		                
		                return 1
		        elif child != parent:
		            return 1
		    return 0
		 
	
		for key in range(len(adj)):
		    if key not in visited:
		        visited.add(key)
		        val = dfs(key,-1)
		        if  val :
		            return 1
	
		return 0
		
