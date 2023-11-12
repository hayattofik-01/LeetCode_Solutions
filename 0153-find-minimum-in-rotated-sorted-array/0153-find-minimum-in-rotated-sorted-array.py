class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # pointers
        left = 0
        right = len(nums) - 1
        min_ = float('inf')
        while left <= right:
            
            #calculate the mid
            mid = left  + (right - left )//2
            min_ = min(min_, nums[mid])
            
            # find the sorted side 
             
            if nums[left] <= nums[mid]:
                min_ = min(min_, nums[left])
                
                left = mid + 1
            else:
                right = mid - 1
        return min_
                
                
        
        
        
       