class Solution:
    def findKthNumber(self,n, k):
        current = 1
        k -= 1

        while k > 0:
            count = 0
            interval = [current, current + 1]

            while interval[0] <= n:
                count += min(n + 1, interval[1]) - interval[0]
                interval = [10 * interval[0], 10 * interval[1]]

            if k >= count:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1

        return current


