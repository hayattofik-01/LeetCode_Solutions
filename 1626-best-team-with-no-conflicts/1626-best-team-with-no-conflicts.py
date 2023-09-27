class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        paired = [[scores[i],ages[i]] for  i in range(len(scores))]
        paired.sort()
        dp = [paired[i][0] for i in range(len(scores))]
        
        for i in range(len(scores)):
            score,age = paired[i]
            for j in range(i):
                tsc , tag = paired[j]
                
                if age >= tag:
                    dp[i] = max(dp[i],score + dp[j])
        return max(dp)
                
                
                