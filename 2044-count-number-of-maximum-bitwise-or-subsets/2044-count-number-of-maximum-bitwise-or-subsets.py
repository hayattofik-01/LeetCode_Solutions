class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        Max = 0
        for num in nums:
            Max  |= num
        
        result = 0
        def backtrack(index,cur_or):
            nonlocal result
            if cur_or == Max:
                result += 1
            for begin in range(index,len(nums)):
                backtrack(begin + 1, cur_or | nums[begin])
        backtrack(0,0)
        return result