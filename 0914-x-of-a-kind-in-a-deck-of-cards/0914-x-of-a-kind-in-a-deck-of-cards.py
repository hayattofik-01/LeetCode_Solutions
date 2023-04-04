class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b ==0:
                return a
            if a == 0 :
                return b
            if a== b:
                return b
            if a > b:
                return gcd(a-b,b)
            return gcd(a,b-a)
        
            
        check = Counter(deck)
        
        prev = check[deck[0]]
        
        for key in check:
            prev = gcd(prev,check[key])
        if prev ==1:
            return False
        return True
           
                
            