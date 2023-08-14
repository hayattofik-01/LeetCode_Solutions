from collections import defaultdict
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjList = defaultdict(list)
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()
        self.sec = 0

        def dfs(start):
            if start in visited or not adjList[start]:
                return 0

            visited.add(start)
            total_sec = 0
            for child in adjList[start]:
                if child not in visited:
                    subtree_sec = dfs(child)
                    if subtree_sec or hasApple[child]:
                        self.sec += 2 + subtree_sec
                        total_sec += 2 + subtree_sec

            return total_sec

        return dfs(0)
       