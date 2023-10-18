class Solution:
    def countPrimes(self, n: int) -> int:

        
        prime = [True for i in range(n)]
   
        
        p = 2
        while (p * p <= n): 
  
        # If prime[p] is not 
        # changed, then it is a prime 
            if (prime[p] == True): 

                # Update all multiples of p 
                for i in range(p * p, n, p): 
                    prime[i] = False
            p += 1
  
        count = 0

        for i in range(2,len(prime)):
            if prime[i]:
                count +=1
        return count
        