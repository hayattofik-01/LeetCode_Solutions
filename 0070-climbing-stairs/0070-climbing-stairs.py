class Solution:
    
    def climbStairs(self, n: int) -> int:
        # at 0th stair
        n1 = 1
        # at 1st stair
        n2 = 1
        
        for i in range(2,n + 1):
            val = n1 + n2 
            n1 = n2 
            n2 = val 
        return n2
     