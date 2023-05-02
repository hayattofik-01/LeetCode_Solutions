def isSink(num,grid):
    for i in range(len(grid)):
        if grid[num][i] != 0:
            return False
    return True
def isSource(num,grid):
    for i in range(len(grid[0])):
        if grid[i][num] !=0:
            return False
    return True
grid= []
size = int(input())
for i in range(size):
    li = list(map(int,input().split()))
    grid.append(li)
sources = []
sinks = []
for i in range(size):
    if isSource(i,grid):
        sources.append(i+1)
    if isSink(i,grid):
        sinks.append(i+1)
print(len(sources), *sources)
print(len(sinks),*sinks)
