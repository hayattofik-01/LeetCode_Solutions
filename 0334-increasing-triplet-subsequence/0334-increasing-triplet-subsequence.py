class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        stack =[(nums[0],0)]
        
        nextGreater = [float('-inf') for i in range(len(nums))]
        prevSmall = [float('-inf') for i in range(len(nums))]
        
        for  i in range(1,len(nums)):
           
            while stack and  stack[-1][0] < nums[i]:
                val = stack.pop()
                nextGreater[val[1]] = nums[i]
        
            stack.append((nums[i],i))
        for i in range(len(nums)-1,-1,-1):
            while stack and  stack[-1][0] > nums[i]:
                val = stack.pop()
                prevSmall[val[1]] = nums[i]
        
            stack.append((nums[i],i))
    
      
        for l , s  in zip(nextGreater,prevSmall):
            
            if l != float('-inf') and s != float('-inf'):
                return True
        return False
        
            
        
        
        
        
        
        
        
        
            
      
       