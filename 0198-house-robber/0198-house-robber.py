class Solution:
    def rob(self, nums: List[int]) -> int:
       
        self.memo =defaultdict(int)
        def rob(h):
            
            if h >= len(nums) :
                return 0
            if h in self.memo:
                return self.memo[h]
            
            self.memo[h] = max(nums[h] + rob(h+2),rob(h+1))
            
            return self.memo[h]
        
        return rob(0)
            
            
        
        
        
        
        
        
        