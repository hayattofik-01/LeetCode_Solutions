class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.adj_lis = defaultdict(list)
        self.visited = set()
       
        

    def birth(self, parentName: str, childName: str) -> None:
        self.adj_lis[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.visited.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        self.inherO = []
        
        def dfs(node):
            if node not in self.visited:
            
                self.inherO.append(node)
            
            for child in self.adj_lis[node]:
                
         
                dfs(child)

                    
       
        dfs(self.king)
        
        return self.inherO
                    
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()