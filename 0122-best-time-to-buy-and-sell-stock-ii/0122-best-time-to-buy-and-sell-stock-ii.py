class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > cur:
                profit += (prices[i] - cur)
            cur = prices[i]
        return profit
                
        
        