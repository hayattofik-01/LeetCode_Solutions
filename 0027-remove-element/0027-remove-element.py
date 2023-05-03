class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            nums[k]=nums[i]
            k+=1
        return k
#         ptr = len(nums)-1
#         for i in range(len(nums)):
#             while(nums[ptr] == val and ptr >= 0):
#                 nums[ptr] = "_"
#                 ptr -=1
#             if nums[i] == val:
#                 nums[i],nums[val] = nums[val],nums[i]
#                 nums[val] = "_"
#         return  nums
        
        
                
        