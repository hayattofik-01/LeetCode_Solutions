class Solution:
    def isGood(self, nums: List[int]) -> bool:
        base=len(nums)-1
        hashmap=defaultdict(int)
        for i in nums:
            if(i>base):
                return False
            hashmap[i]+=1
            if(i!=base and hashmap[i]>1):
                return False
        if(hashmap[base]>2):
            return False
        else:
            return True
        