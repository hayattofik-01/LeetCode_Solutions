class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        Max = nums[0]
        Sum = nums[0]
        for  i in range(1,len(nums)):
            Sum +=nums[i]
            curr = nums[i]
            if curr > Max :
                Max = max(Max , math.ceil(Sum/(i+1))) 
        return Max
                
                
        
     