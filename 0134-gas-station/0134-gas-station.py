class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        profit = [g -c for g,c in zip(gas,cost)]
        
        if sum(profit) < 0:
            return -1
    
        ans = 0
        gain = 0
        for i in range(len(profit)):
            gain += profit[i]
            if gain < 0:
                gain = 0
                ans = i + 1
            

        return ans 
            
                
            
        
        
            
        
        