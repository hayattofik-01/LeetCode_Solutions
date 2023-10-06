class Trie:
    def __init__(self):
        self.children = {}
        self.idx = -1

class WordFilter(object):

    def __init__(self, words):
    
        self.trie = Trie()
        
        for idx, word in enumerate(words):
            self.addWord(idx, word)
    
    def addWord(self, idx, word):
        for i in range(len(word)-1, -2, -1):
            newString = word[i+1:] + '#' + word
            node = self.trie
            node.idx = idx
            
            for letter in newString:
                if letter not in node.children:
                    node.children[letter] = Trie()
                node = node.children[letter]
                node.idx = idx
        

    def f(self, prefix, suffix):
    
        node = self.trie
        newString = suffix + '#' + prefix
        
        for letter in newString:
            if letter not in node.children:
                return -1
            node = node.children[letter]
        
        return node.idx


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)