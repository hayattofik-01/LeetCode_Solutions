class Solution:
    def findKthNumber(self,n, k):
        current = 1
        k -= 1  # Decrement k to account for the first number we start with

        while k > 0:
            count = 0

            # Calculate the count of numbers between current and current + 1
            interval_start = current
            interval_end = current + 1

            while interval_start <= n:
                count += min(n + 1, interval_end) - interval_start
                interval_start *= 10
                interval_end *= 10

            if k >= count:
                current += 1  # Move to the next number in the same level
                k -= count
            else:
                current *= 10  # Move to the next level by appending a 0
                k -= 1

        return current

