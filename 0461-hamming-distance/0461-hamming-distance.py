class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # to know the bits they are different with
        difference =  x ^ y
        check = 1
        ham_dis = 0
        
        for i in range(32):
            
            val = difference & check
            if val :
                ham_dis +=1
            check <<= 1
        return ham_dis
                
        
       