class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        que = deque()
        
        def generateChildren(parent):
            children = []
            for i in range(4):
                numA = (int(parent[i])+1)%10
                
                children.append(parent[:i] + str(numA) + parent[i+1:])
                numS = ((int(parent[i])-1 + 10) % 10)
                children.append(parent[:i] + str(numS) + parent[i+1:])
            return children
        que.append(("0000",0))
        if "0000" in visited :
            return -1
        while que:
            node,level = que.popleft()
            if node == target:
                return level
           
            for child in generateChildren(node):
                if child not in visited :
                    que.append((child,level+1))
                    visited.add(child)
        return -1