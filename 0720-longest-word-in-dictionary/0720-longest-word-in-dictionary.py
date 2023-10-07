class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True

    def dfs(self, node, curr_word):
        longest_word = ''
        if node.isWord:
            longest_word = curr_word
        
        for char in node.children:
            if node.children[char].isWord:
                word = self.dfs(node.children[char], curr_word + char)
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        return longest_word



class Solution:
    def longestWord(self,words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        longest_word = trie.dfs(trie.root, '')
        
        return longest_word
    