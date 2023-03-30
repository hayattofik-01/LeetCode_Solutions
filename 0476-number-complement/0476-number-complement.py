class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while(i <=num):
            i= i << 1
        candidate = i - 1
        
        return (num ^ candidate)
         
        
       
        
        