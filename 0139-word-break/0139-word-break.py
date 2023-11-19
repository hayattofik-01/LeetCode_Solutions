class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False for idx in range(len(s) + 1)]
        
        dp[len(s)] = True
        
        for let in range(len(s) - 1 , -1, -1):
            
            for word in wordDict:
                
                if (let + len(word)) <= len(s) and s[let: let + len(word)] == word:
                    
                    dp[let] = dp[let + len(word)]
                    
                if dp[let] :
                    break
        return dp[0]
                
        