class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = defaultdict(int)
        for i in range(n):
            parent[i] = i
        
        def find(a):
            
            while parent[a] != a:
                a = parent[a]
            return a
        
        def union (a,b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA != rootB:
                parent[rootA] = rootB
       
       
        for num1, num2 in edges:
            union(num1,num2)
       
        if find(source) == find(destination):
            return True
        return False
            
            
            
            