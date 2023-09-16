class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(start, count):
            nonlocal max_requests
            if start == len(requests):
                if checkZeros(check):
                    max_requests = max(max_requests, count)
                return

            # Take the request
            check[requests[start][0]] -= 1
            check[requests[start][1]] += 1
            backtrack(start + 1, count + 1)

            # Skip the request
            check[requests[start][0]] += 1
            check[requests[start][1]] -= 1
            backtrack(start + 1, count)

        def checkZeros(lists):
            for i in lists:
                if i != 0:
                    return False
            return True

        max_requests = 0
        check = [0] * n
        backtrack(0, 0)
        return max_requests