class Solution:
   
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     
    
        
        freMap={}
        output=[]
        tmp=[]
        for i in range(len(nums)):
            if nums[i] in freMap:
                freMap[nums[i]]+=1
            else:
                freMap[nums[i]]=1
        values=list(freMap.values())
        values.sort()
        values.reverse()
        for i in range(k):
            tmp.append(values[i])
        for num in freMap:
            if freMap[num] in tmp:
                output.append(num)
        return output

       
      


           