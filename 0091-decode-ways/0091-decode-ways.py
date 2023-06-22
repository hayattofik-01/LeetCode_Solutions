class Solution:
    def numDecodings(self, s: str) -> int:
       
            memo = {}
            def dfs(i):
                if i in memo:
                    return memo[i]
                if i == len(s):
                    return 1
                if s[i] == '0':
                    return 0
                res = dfs(i+1)
                if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    res += dfs(i+2)
                memo[i] = res
                return res
            return dfs(0)
    
        