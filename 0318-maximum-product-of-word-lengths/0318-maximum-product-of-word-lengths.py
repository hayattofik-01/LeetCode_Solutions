class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def getBitmask(word):
            bitmask = 0
            for char in word:
                bitmask |= 1 << ord(char)
            return bitmask

        word_bitmasks = {}
        for word in words:
            word_bitmasks[word] = getBitmask(word)

        max_product = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if word_bitmasks[words[i]] & word_bitmasks[words[j]] == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product