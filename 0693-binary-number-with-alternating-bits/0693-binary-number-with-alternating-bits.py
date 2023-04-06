class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length=  math.log(n,2)
       
        on = 1
        val = n & on
        on <<=1
        for i in range(ceil(length)):
            check = n & on
            if check and val :
                return False
            if check==0 and val==0:
                return False
            val = check
            on <<=1
        return True
            
            
            
            
            
            
        
        