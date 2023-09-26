class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            
            if not  cur.children[ord(l) - ord('a')]:
                cur.children[ord(l) - ord('a')] = TrieNode()
            cur = cur.children[ord(l) - ord('a')]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if not cur.children[ord(l) - ord('a')]:
                return False
            cur = cur.children[ord(l) - ord('a')]
        if not cur.is_end:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
           
            
            if not cur.children[ord(l) - ord('a')]:
                return False
            cur = cur.children[ord(l) - ord('a')]
       
        return True
        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)