class Solution:
    def mySqrt(self, x: int) -> int:
        best = -1
        l = 0
        r = x
        
        while l <= r :
            mid  = (l + r)//2
            if mid * mid  > x:
                r = mid -1
            else:
                best = mid
                l = mid + 1
           
        return best 
            
        