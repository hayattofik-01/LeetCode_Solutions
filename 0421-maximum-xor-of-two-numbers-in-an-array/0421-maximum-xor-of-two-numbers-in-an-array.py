class Solution:
    def findMaximumXOR(self, nums):
        cmax = 0
        for i in range(31, -1, -1):
            tmp = cmax | (1 << i)
            S = set(tmp & j for j in nums)
            if any(j ^ tmp in S for j in S): 
                cmax = tmp
        return cmax