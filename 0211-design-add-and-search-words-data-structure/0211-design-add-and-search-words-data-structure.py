class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if not cur.children[ord(l) - ord('a')]:
                cur.children[ord(l) - ord('a')] = TrieNode()
            cur = cur.children[ord(l) - ord('a')]
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self.searchRecursive(word, self.root)

    def searchRecursive(self, word: str, node) -> bool:
        if not word:
            return node.is_end

        if word[0] == '.':
            for child in node.children:
                if child and self.searchRecursive(word[1:], child):
                    return True
            return False

        if not node.children[ord(word[0]) - ord('a')]:
            return False

        return self.searchRecursive(word[1:], node.children[ord(word[0]) - ord('a')])


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False