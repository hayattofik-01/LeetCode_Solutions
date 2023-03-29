class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.output = set()
        
        def dfs(cur,li):
            if cur >= len(nums):
                if len(li) >= 2:
                    self.output.add(tuple(li))
                return 
            
            #pick
            if not li or li[-1] <= nums[cur]:
                li.append(nums[cur])
                dfs(cur + 1,li)
                li.pop()
           
            dfs(cur+1,li)
            
        dfs(0,[])
        return self.output   
                
            
           
            
           
        
#     
        