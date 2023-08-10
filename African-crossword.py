from collections import defaultdict


n,m = map(int,input().split())
grid = []
for i in range(n):
    rw = input()
    li= []
    for let in rw:
        li.append(let)
    grid.append(li)
rowRef = defaultdict(int)
colRef = defaultdict(int)

for row in range(len(grid)):
    for col in range(len(grid[0])):
        rowRef[(grid[row][col],row)] +=1
        colRef[(grid[row][col],col)] +=1
ans = ""
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if rowRef[(grid[row][col],row)] > 1 or colRef[(grid[row][col],col)] > 1:
            grid[row][col] = None
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col]:
            ans +=grid[row][col]

print(ans)
