import heapq as hq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        def count_till_one(num):
            count = 0
            while num != 1:
              
                if num in dp:
                    return count + dp[num]
                if num % 2 == 0:
                    num = num//2
                else:
                    num = 3 * num + 1
                count +=1
            return count
        output = []
     
        for num in range(lo,hi + 1):
            count = count_till_one(num)
            dp[num] = count
            if len(output) == k:
                output.append(num)

            else:
                output.append(num)
        output.sort(key = lambda a : dp[a])
        
    
        return output[k - 1]