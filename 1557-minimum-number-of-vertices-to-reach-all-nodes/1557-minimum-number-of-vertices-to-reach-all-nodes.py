class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        inDegree= [0 for i in range(n)]
        adj_lis = defaultdict(list)
        visited = set()
        
        for fr ,to in edges:
            adj_lis[fr].append(to)
            inDegree[to] +=1
        
        que = deque()
        output = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                output.append(i)
                que.append(i)
                visited.add(i)
        
        
        def bfs(que):
            while que:
                node = que.popleft()
                
                
                for child in adj_lis[node]:
                    inDegree[child]-=1
                    
                    if inDegree[child] == 0:
                        que.append(child)
                        visited.add(child)
        bfs(que)
    
        for i in range(n):
            if i not in visited:
                output.append(i)
        return output
        
                
            
        