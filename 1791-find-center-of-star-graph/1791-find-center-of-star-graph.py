class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj_lis = defaultdict(list)
        
        for i,d in edges:
            adj_lis[i].append(d)
            adj_lis[d].append(i)
        
        for node in adj_lis:
            if len(adj_lis[node]) == len(adj_lis) -1:
                return node
        