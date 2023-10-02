class MapSum:

    def __init__(self):
        self.trie = {}
        self.keyRef = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        self.keyRef[key] = val
        for char in key:
            if char not in cur:
                cur[char] = {'pas': [key]}
            else:
                cur[char]['pas'].append(key)
            cur = cur[char]
        

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return 0
        ans = 0
        check = set(cur['pas'])
        for val in check:
            ans += self.keyRef[val]
        return ans
        
            
                
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)