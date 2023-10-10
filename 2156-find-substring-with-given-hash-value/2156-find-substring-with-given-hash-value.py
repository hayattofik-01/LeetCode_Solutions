class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        curhash = 0
        pow_ = 1
        for i in range(k):
            curhash += ( (ord(s[i]) - ord('a') ) + 1 )  * pow_
            
            pow_ *= power
        
        l = 0
        
        if (curhash % modulo) == hashValue:
            return s[l:k]
        pow_ = power**(k - 1)
        for r in range(k,len(s)):
            
            
            curhash -= (ord(s[l]) - ord('a')) + 1 
            curhash //= power
            
            curhash += ( (ord(s[r]) - ord('a')) + 1)* pow_
            l +=1
            if (curhash % modulo) == hashValue:
                return s[l :r + 1 ]
            
            
        
           
            

            