class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        for i,j in  zip(s1,s2):
            parent[i]= i
            parent[j]  = j

        def find(cell):

                    if parent[cell] != cell:
                        parent[cell] = find(parent[cell])

                    return parent[cell]
            
                
                

        def union(cell1,cell2):

            rootC1 = find(cell1)
            rootC2 = find(cell2)

            if rootC1 != rootC2:

                if rootC1 > rootC2:
                    parent[rootC1] = rootC2

                else:
                    parent[rootC2] = rootC1
            
        for i,j in zip(s1,s2):
            union(i,j)
        baseSt = []
        for l in baseStr:
            baseSt.append(l)
            
        for i in range(len(baseSt)):
            if baseSt[i] in parent:
                baseSt[i]=find(baseSt[i])
           
        return "".join(baseSt)
            
            
        
        
            
