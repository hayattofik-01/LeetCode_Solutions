class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        
        for a,b,w in flights:
            adj_list[a].append((b,w))
            
        que = [(0,0,src)]
        
        visited = set()
        while que:
            price,ks, node = heappop(que)
            if node == dst:
                return price
            if (node,ks) in visited:
                continue
            visited.add((node,ks))
            
            for child,weight in adj_list[node]:
                
                if ks < k or child == dst:
                    heappush(que,(weight + price,ks + 1,child))
        return -1
            
                
                
            
        
        