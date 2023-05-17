class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict(int)
        
        for i in range(1,len(edges) + 1):
            parent[i] = i
        
        
        def find(node ):
            
            while parent[node] != node:
                node = parent[node]
            return node
        def union(n1, n2):
            rootN1 = find(n1)
            rootN2 = find(n2)
            
            if rootN1 != rootN2:
                parent[rootN1] = rootN2
                return False
            return True
        
        for n1,n2 in edges:
            
            check = union( n1 , n2)
            
            if check:
                return [n1,n2]
        
        
            
        