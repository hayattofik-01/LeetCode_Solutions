class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        refer = defaultdict(int)
        for n in nums:
            refer[n] +=1
        for k in refer:
            if refer[k] > len(nums)//2:
                return k
        
        