class Solution:

    def tribonacci(self, n: int,memo = defaultdict(int)) -> int:
        
        if n == 0:
            return 0
        if n <=  2:
            return 1
        if n in memo:
            return memo[n]
        
        memo[n] =  self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
        return  memo[n]