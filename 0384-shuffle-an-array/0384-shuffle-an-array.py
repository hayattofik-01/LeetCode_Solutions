class Solution:

    def __init__(self, nums: List[int]):
        self.original  = nums

        

    def reset(self) -> List[int]:
        
        return self.original
        

    def shuffle(self) -> List[int]:
        
        shuffled = self.original.copy()
        for idx in range(len(self.original)):
            
            nidx = random.randrange(idx ,len(shuffled))
            shuffled[idx],shuffled[nidx] = shuffled[nidx], shuffled[idx]
        return shuffled
        
        
       
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()