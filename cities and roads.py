n = int(input())
grid = []
for i in range(n):
    arr = list(map(int,input().split()))
    grid.append(arr)
count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            count +=1
            grid[j][i] = 0
print(count)
