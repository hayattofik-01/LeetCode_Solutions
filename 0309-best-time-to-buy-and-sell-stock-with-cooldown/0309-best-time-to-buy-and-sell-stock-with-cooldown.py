class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # dp=[[0]*2 for i in range(n+2)]
        ahd=[0]*2
        ahd2=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2
            for buy in range(2):
                if buy:
                    curr[buy]=max(ahd[buy],ahd[0]-prices[i])
                else:
                    curr[buy]=max(ahd[buy],ahd2[1]+prices[i])
            ahd2=ahd[:]
            ahd=curr[:]
        return ahd[1]
        