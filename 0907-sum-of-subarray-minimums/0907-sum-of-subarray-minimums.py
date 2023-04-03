class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
       
        res = 0
        stack = []
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[i] < arr[stack[-1]]): 
                mid = stack.pop()
                left = -1 if not stack else stack[-1] # small than mid (left)
                right = i # small than mid right one
                res += ((mid - left) * (right - mid) * arr[mid])
            stack.append(i)
        return res % (10 ** 9 + 7)
        