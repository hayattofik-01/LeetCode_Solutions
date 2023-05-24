class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if k < numOnes:
            return k
        elif numZeros  + numOnes >=k:
            return numOnes
        else:
            temp = k-numOnes-numZeros
            numOnes-=temp
            return numOnes