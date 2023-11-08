class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        # the sum that we could find by choosing a candidate value from values 1 - max(arr)
        def candidateSum(candidate):
            curSum = 0
            
            for num in arr:
                if num > candidate:
                    curSum += candidate
                else:
                    curSum += num
            return curSum
        # binary search on the values 1 - max(arr)
        
        start = 1
        end = max(arr) 
        
        while start <= end:
            
            mid = start + (end - start)//2
            candidate_sum = candidateSum(mid)
            
            # if it is equal to target that is the best candidate
            if candidate_sum == target : return mid
            
            # if candidate sum is less than target - search for bigger value 
            elif candidate_sum < target : 
                start = mid + 1
            # if candidate sum is greater that target  try to find the minumum integer
            else:
                end = mid  - 1
        start_sum = candidateSum(start)
        end_sum = candidateSum(end)
        print(start_sum, end_sum)
        print(start,end)
        
        if abs(target - start_sum) < abs(target - end_sum):
            return start
        else:
            return end
        
                    
            
            
        