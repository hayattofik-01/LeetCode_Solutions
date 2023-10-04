class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list= defaultdict(list)
        
        for a,b,w in times:
            adj_list[a - 1].append((w,b - 1))
        distances = [float('inf') for i in range(n)]
        distances[k - 1] = 0
        
        que = []
        heapify(que)
        que.append((0,k - 1))
        visited = set()
        
        while que:
            distance , node = heappop(que)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            for w,c in adj_list[node]:
                
                temp_dis = w + distance
                
                if temp_dis < distances[c]:
                    distances[c] = temp_dis
                
                heappush(que,(distances[c],c))

        val  = max(distances)
        if val == float('inf'):
            return -1
        return val
                
        
        