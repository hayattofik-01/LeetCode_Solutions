class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
       
        for k in range(n+1):
            i = 1
            count = 0
            
            for j  in range(32):
                val = k & i
                if val !=0:
                    count+=1
                i = i << 1
                
            output.append(count)
        return output
            
            
        