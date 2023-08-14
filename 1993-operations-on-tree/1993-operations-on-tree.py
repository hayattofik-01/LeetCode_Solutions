
class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.adjList = defaultdict(list)
        for i in range(len(parent)):
            self.adjList[parent[i]].append(i)
        self.isLocked = [0] * len(parent)
        self.lockedDescendants = [0] * len(parent)

    def lock(self, num: int, user: int) -> bool:
        if self.isLocked[num] == 0:
            self.isLocked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.isLocked[num] == user:
            self.isLocked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if self.isLocked[num] == 0 and self.hasLockedDescendant(num) and not self.hasLockedAncestor(num):
            self.unlockDescendants(num)
            self.isLocked[num] = user
            return True
        return False

    def hasLockedDescendant(self, num: int) -> bool:
        for child in self.adjList[num]:
            if self.isLocked[child] != 0 or self.hasLockedDescendant(child):
                return True
        return False

    def hasLockedAncestor(self, num: int) -> bool:
        curr = num
        while self.parent[curr] != -1:
            if self.isLocked[self.parent[curr]] != 0:
                return True
            curr = self.parent[curr]
        return False

    def unlockDescendants(self, num: int):
        for child in self.adjList[num]:
            self.isLocked[child] = 0
            self.unlockDescendants(child)