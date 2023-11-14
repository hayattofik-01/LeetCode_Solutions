import random
class RandomizedSet:

    def __init__(self):
        self.numToIdx = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        if val in self.numToIdx:
            return False
        self.numList.append(val)
        self.numToIdx[val] = len(self.numList)  - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numToIdx :
            return False
        index = self.numToIdx[val]
        
        self.numToIdx[self.numList[-1]] = index
        del self.numToIdx[val]
        self.numList[index],self.numList[-1] = self.numList[-1],self.numList[index]
        self.numList.pop()
        return True
        

    def getRandom(self) -> int:
        randomVal = random.choice(self.numList)
        return randomVal
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()