class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        notEqual = set()
        parent= defaultdict(str)
        size ={}
        for i in range(26):
            parent[chr(i + 97)] = chr(i + 97)
            size[chr(i + 97)] = 1
        def find(val):
            
            if parent[val] != val:
                
                val = find(parent[val])
            return val
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA != rootB:
                if size[rootA] > size[rootB]:
                    parent[rootB] = rootA
                    size[rootB] +=size[rootA]
                else:
                    parent[rootA] = rootB
                    size[rootA] +=size[rootB]
                    
            
            
                
            
            
        for exp in equations:
            if exp[1] == "!":
                notEqual.add((exp[0],exp[3]))
            else:
                union(exp[0],exp[3])
        for a,b in notEqual:
            if find(a) == find(b):
                return False
        return True
                
        