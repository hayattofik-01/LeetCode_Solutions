class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 0
        for i in range(n):
            result += self.numTrees(i)*self.numTrees(n-i-1)
        return result
        