class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.randomset = []
    
       

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val]= len(self.randomset) 
        self.randomset.append(val)
        return True
        

    def remove(self, val: int) -> bool:
       
        if val not in self.index:
            return False
            
        index = self.index[val]

        self.index[self.randomset[-1]] = index
        self.randomset[-1],self.randomset[index] = self.randomset[index],self.randomset[-1]
        self.randomset.pop()
        del self.index[val]

    
        return True
        
        

    def getRandom(self) -> int:
        
        val = random.choice(self.randomset)

        return val
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()