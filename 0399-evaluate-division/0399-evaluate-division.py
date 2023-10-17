class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        def calculateCost(start,end):
            if start not in adj_list or end not in adj_list :
                return -1
            que  = deque()
            que.append((start,1))
            visited = set()
            visited.add(start)
            while que:
                n,w = que.popleft()
             
                if n == end:
                    
                    return w
                for child,wc in adj_list[n]:
                    if child not in visited:
                        que.append((child,wc * w))
                        visited.add(child)
            return - 1
        for i,a in enumerate(equations):
            adj_list[a[0]].append((a[1],values[i]))
            adj_list[a[1]].append((a[0],(1/values[i])))
                                 
        ans = []
                                   
        for a , b in queries:
            ans.append(calculateCost(a,b))
        return ans
                        
    
                                   
                                  
                
        