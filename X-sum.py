siz = int(input())

def inBound(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def score1(i,j,grid):
    add = 0
    i -=1
    j-=1
    while inBound(i,j,len(grid),len(grid[0])):
        add += grid[i][j]
        i -=1
        j-=1
    return add 
def score2(i,j,grid):
    add = 0
    i +=1
    j-=1
    while inBound(i,j,len(grid),len(grid[0])):
        add += grid[i][j]
        i +=1
        j-=1
    return add
def score3(i,j,grid):
    add = 0
    i -=1
    j+=1
    while inBound(i,j,len(grid),len(grid[0])):
        add += grid[i][j]
        i -=1
        j+=1
    return add

def score4(i,j,grid):
    add = 0
    i +=1
    j+=1
    while inBound(i,j,len(grid),len(grid[0])):
        add += grid[i][j]
        i +=1
        j+=1
    return add


for _ in range(siz):
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        l = list(map(int, input().split()))
        grid.append(l)
    m = float("-inf")
    for row in range(r):
        for col in range(c):
            val = grid[row][col] + score1(row,col,grid) + score2(row,col,grid) + score3(row,col,grid) + score4(row,col,grid)
            m = max(val, m)
    print(m)
