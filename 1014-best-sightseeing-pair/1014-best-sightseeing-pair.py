class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        '''we want to maximize a[i] + [i] let's call it right
        and we also want to maximize a[j] - j- lets call it left
        first we calculate right and left and then we will be getting maximum out of 2
        '''
        left = [values[0]]
        right = [0]
        for i in range(len(values)):
            if values[i] + i > left[-1]:
                left.append(values[i] + i)
            else:
                left.append(left[-1])
        m = float("-inf")
        for i in range(1,len(values)):
            
            val = values[i] - i 
            m  = max(m,val + left[i])
        return m
            
        