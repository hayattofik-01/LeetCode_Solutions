class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        heapify(heap)
        for stone in stones:
            heappush(heap,-1 * stone)
        
        while  len(heap) > 1:
            y = heappop(heap)
            x= heappop(heap)
          
            if x != y:
                heappush(heap,-1 * (abs(y)-abs(x)))
        if not heap:
            return 0
       
        return abs(heap[0])

        
        
        