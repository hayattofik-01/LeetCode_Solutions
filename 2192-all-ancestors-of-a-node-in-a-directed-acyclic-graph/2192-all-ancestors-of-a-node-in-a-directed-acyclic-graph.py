class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_lis = defaultdict(list)
        output = [set() for i in range(n)]
        visited = set()
        inDegree = [0 for i in range(n)]
        que = deque()
        for fr,to in edges:
            adj_lis[fr].append(to)
            inDegree[to] +=1
        for i in  range(n):
            if inDegree[i] == 0:
                que.append(i)
        while que:
            node = que.popleft()
            
            for child in adj_lis[node]:
                
                inDegree[child] -=1
                output[child].add(node)
                output[child].update(output[node])
                if inDegree[child] == 0:
                    que.append(child)
            
        return [sorted(child) for child in output]
                            
            
        