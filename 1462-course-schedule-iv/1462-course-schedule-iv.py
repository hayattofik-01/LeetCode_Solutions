class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        def search(a,b):
            que = deque()
            visited = set()
            que.append(b)
            while que:
                cur = que.popleft()
                if cur == a:
                    return True
                visited.add(cur)
                for child in adj_list[cur]:
                    if child not in visited:
                        que.append(child)
                    
            return False
                
        ans = []
        for a,b in prerequisites:
            adj_list[b].append(a)
        for a,b in queries:
            ans.append(search(a,b))
        return ans