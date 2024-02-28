class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        need to know how frequent a word - hashmap for counting
        need to now to k frequent words - sort and return top k 
        (TC - nlogn,
        SC - n(for hashmap) )
        
        steps 
        1. count the words 
        2. sort them based on frequency
        3. return the top k elements
        
        Improve sorting by using heap
        2.keep heap of size two and keep adding elements using heappushpop
          
     
        '''
        counter = {}
        counterMate = []
        heapify(counterMate)
        for word in words:
            counter[word] = 1 + counter.get(word,0)
        for word in counter:
            heappush(counterMate,(-counter[word],word))
      
            
        output = []
        
        for i in range(k):
            output.append(heappop(counterMate)[1])
        return output
        
    