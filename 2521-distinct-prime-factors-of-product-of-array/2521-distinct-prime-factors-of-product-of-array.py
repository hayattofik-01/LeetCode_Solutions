class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # Create a list to store prime numbers using the Sieve of Eratosthenes algorithm
        primes = [True] * 1001
        primes[0] = primes[1] = False
        p = 2
        while p * p <= 1000:
            if primes[p]:
                for i in range(p * p, 1001, p):
                    primes[i] = False
            p += 1

        # Calculate the product of all the elements in nums
        val = 1
        for n in nums:
            val *= n

        # Check the number of distinct prime factors
        ans = 0
        for num in range(2, 1001):
            if primes[num]:
                if val % num == 0:
                    ans += 1
                    while val % num == 0:
                        val //= num
                if val == 1:
                    break

        return ans