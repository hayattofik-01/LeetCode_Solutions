class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_lis = defaultdict(list)
        inDegree = [0 for i in range(len(quiet))]
        que= deque()
        output= [i for i in range(len(quiet))]
        for a, b in richer:
            adj_lis[a].append(b)
            inDegree[b] +=1
      
        for i in range(len(inDegree)):
            if not inDegree[i]:
                que.append(i)
       
        while que:
            
            parent = que.popleft()
            check = quiet[parent]
            
            for child in adj_lis[parent]:
                if check  < quiet[child]:
                    quiet[child] = check
                    output[child] = output[parent]
            
                inDegree[child] -=1
              
                if inDegree[child] == 0:
                    que.append(child)
        return output
                
            
        