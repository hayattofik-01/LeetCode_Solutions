class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = [[0 for i in range(len(s))]for j in range(len(s))]
        reverse = s[::-1]
        
        for up in range(len(s)):
            for side in range(len(s)):
                if s[up] == reverse[side]:
                    if up and side:
                        cache[up][side] = cache[up - 1][side  - 1] + 1
                    else:
                        cache[up][side] = 1
                else:
                    cache[up][side] = max(cache[up-1][side] if up else 0 , cache[up][side - 1] if side else 0)
        return cache[len(s)-1][len(s)-1]
                    
        
        