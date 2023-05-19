class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_lis = defaultdict(list)
        
        for n1,n2,w in roads:
            adj_lis[n1].append(n2)
            adj_lis[n2].append(n1)
        visited= set()   
       
        que= deque()
        que.append(1)
        visited.add(1)

        while que:
            node = que.popleft()

            for child in adj_lis[node]:

                if child not in visited:
                    que.append(child)
                    visited.add(child)
        Min = float('inf')
        for i,j,w in roads:
            
            if i in visited and j in visited:
                Min = min(Min,w)
                
        return Min
        
        
#         root = defaultdict(int)
#         size = [1 for i in range(n)]
#         ans = [float('inf') for i in range(n)]
#         for i in range(n):
#             root[i]= i
        
#         def find(x):
            
#             while root[x] != x:
#                 x = root[x],jm m
                
            
                
            
        
      