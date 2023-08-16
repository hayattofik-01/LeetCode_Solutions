from collections import defaultdict


noV = int(input())
noP= int(input())
adjList = defaultdict(list)
for i in range(noP):
    op = list(map(int,input().split()))
    if op[0] == 2:
        
        print(*adjList[op[1]])
    else:
        
        adjList[op[2]].append(op[1])
        adjList[op[1]].append(op[2])
