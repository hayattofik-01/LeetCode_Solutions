class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapSize = 0
        for n in nums:
            
         
            heappush(heap,n)
            heapSize +=1
            if heapSize > k:
                heappop(heap)
                heapSize -=1
        return heappop(heap)
        