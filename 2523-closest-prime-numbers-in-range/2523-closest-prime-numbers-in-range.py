class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        #sieves algorithm
        p = 2
        primes = [True for i in range(right + 1 )]
        primes[0] = False
        
        
        while(p * p <= right):
                if primes[p]:
                    for i in range(p * p, right + 1, p):
                        primes[i] = False # mark all multiples except for the first number as non-prime
                p += 1
    
            
        que = deque()
        ans = float('inf')
        nums = [ -1,-1]
        primes[1] = False

        for i in range(left,right + 1):
            if primes[i] :
                que.append(i)
        
            if len(que) == 2:
                val =(que[1] - que[0])
                if val < ans:
                    ans = val
                    if left <= que[0] < que[1] <= right:
                        nums = [que[0],que[1]]
                que.popleft()
        return nums
                
                
                
        
        